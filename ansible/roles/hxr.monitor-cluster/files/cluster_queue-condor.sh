#!/bin/bash
condor_q | grep "all\|Schedd" | while read -r hostline; read -r numbersline; do
    # Extract the host name
    host=$(echo "$hostline" | awk -F": " '{gsub(/ /, "", $2); print $2}');
    
    # Process the numbers line
    echo "$numbersline" | sed 's/.* jobs;\s*//g;s/, /\n/g' | while read -r line; do
        # Extract the type and count of jobs
        type=$(echo "$line" | sed 's/^[0-9]* //g');
        count=$(echo "$line" | sed 's/ .*//g');
        
        # Print the formatted output
        echo "cluster.queue,engine=condor,schedd=\"$host\",state=$type count=$count"
    done;
done;


# condor_q -global -total | grep "all\|Schedd"  | while read hostline; read numbersline; do
#     host=$(echo $hostline | awk -F": " '{gsub(/ /, "", $2); print$2}');
#     echo $numbersline | sed 's/.* jobs;\s*//g;s/, /\n/g' | while read line; do
#         type=$(echo $line | sed 's/^[0-9]* //g');
#         count=$(echo $line | sed 's/ .*//g');
#         echo cluster.queue,engine=condor,schedd="$host",state=$type count=$count
#     done;
# done;
