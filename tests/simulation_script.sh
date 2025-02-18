#!/bin/bash

INFLUXDB_HOST="influxdb"
INFLUXDB_PORT="8086"
INFLUXDB_USER="esg"
INFLUXDB_PASS=""
INFLUXDB_DB="db"

# Destination IDs
destinations=(
    "pulsar_de02" "pulsar_cz01" "pulsar_it01" "pulsar_sp01" "pulsar_uk01"
    "pulsar_tr01" "pulsar_no01" "pulsar_pl01" "pulsar_ch01" "pulsar_sl01"
)

# Initial values
declare -A avg_queue=( [trinity]=4.0 [spades]=15.0 [bwa]=3.5 [hisat2]=6.5 [bowtie2]=10.5 )
declare -A avg_run=( [trinity]=2400 [spades]=7200 [bwa]=3600 [hisat2]=5400 [bowtie2]=7200 )

# Function to generate small floating-point variations
generate_float_variation() {
    local base=$1
    local min_change=-2.0
    local max_change=2.0
    local variation=$(awk -v min="$min_change" -v max="$max_change" 'BEGIN{srand(); print min+rand()*(max-min)}')
    echo "$(echo "$base + $variation" | bc)"
}

# Function to generate small integer variations
generate_int_variation() {
    local base=$1
    local min_change=-2
    local max_change=2
    local variation=$(( RANDOM % (max_change - min_change + 1) + min_change ))
    echo $(( base + variation ))
}

# Process each destination
for dest in "${destinations[@]}"; do
    for tool in "trinity" "spades" "bwa" "hisat2" "bowtie2"; do
        queue=$(generate_float_variation ${avg_queue[$tool]})
        run=$(generate_int_variation ${avg_run[$tool]})
        insert_statement="INSERT destination-queue-run-time,destination_id=$dest,host=test.usegalaxy.be,tool_id=$tool count=5,avg_queue=$queue,min_queue=2,median_queue=3.5,perc_95_queue=7,perc_99_queue=8,max_queue=10,avg_run=$run,min_run=200,median_run=1800,perc_95_run=4000,perc_99_run=4500,max_run=5000"
        #echo "$insert_statement"
        influx -host "$INFLUXDB_HOST" -port "$INFLUXDB_PORT" -username "$INFLUXDB_USER" -password "$INFLUXDB_PASS" -database "$INFLUXDB_DB" -ssl -execute "$insert_statement"
    done

    # Insert queue states for each destination
    queue_statement="INSERT queue_by_destination,destination_id=$dest,host=test.usegalaxy.be,state=queued count=$(generate_int_variation 8)"
    #echo "$queue_statement"
    influx -host "$INFLUXDB_HOST" -port "$INFLUXDB_PORT" -username "$INFLUXDB_USER" -password "$INFLUXDB_PASS" -database "$INFLUXDB_DB" -ssl -execute "$queue_statement"

    running_statement="INSERT queue_by_destination,destination_id=$dest,host=test.usegalaxy.be,state=running count=$(generate_int_variation 4)"
    #echo "$running_statement"
    influx -host "$INFLUXDB_HOST" -port "$INFLUXDB_PORT" -username "$INFLUXDB_USER" -password "$INFLUXDB_PASS" -database "$INFLUXDB_DB" -ssl -execute "$running_statement"
done