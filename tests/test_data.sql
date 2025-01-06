-- Test data inserts for below set of destination_ids inserted on 2025-01-06T10:59:23

-- destination_id:
-- condor_tpv  
-- condor_us  
-- pulsar_be01  
-- pulsar_us01  
-- pulsar_eu01  
-- pulsar_asia01
-- pulsar_fr
-- pulsar_fr01_tpv
-- pulsar_de
-- pulsar_in
-- pulsar_cz01_tpv
-- pulsar_sk01_tpv
-- pulsar_uk

-- htcondor_cluster_usage
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=0,unclaimed_cpus=32,total_memory=64000,claimed_memory=0,unclaimed_memory=64000,total_loadavg=0,claimed_loadavg=0,unclaimed_loadavg=0,total_slots=4,claimed_busy_slots=0,unclaimed_idle_slots=4,querytime=1730910000,destination_id="condor_tpv",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=16,unclaimed_cpus=16,total_memory=64000,claimed_memory=32000,unclaimed_memory=32000,total_loadavg=8.0,claimed_loadavg=4.0,unclaimed_loadavg=4.0,total_slots=4,claimed_busy_slots=2,unclaimed_idle_slots=2,querytime=1730910100,destination_id="condor_us",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=30,unclaimed_cpus=2,total_memory=64000,claimed_memory=62000,unclaimed_memory=2000,total_loadavg=29.5,claimed_loadavg=15.0,unclaimed_loadavg=14.5,total_slots=4,claimed_busy_slots=3,unclaimed_idle_slots=1,querytime=1730910200,destination_id="pulsar_be01",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=10,unclaimed_cpus=22,total_memory=64000,claimed_memory=20000,unclaimed_memory=44000,total_loadavg=15.0,claimed_loadavg=7.5,unclaimed_loadavg=7.5,total_slots=4,claimed_busy_slots=2,unclaimed_idle_slots=2,querytime=1730910300,destination_id="pulsar_us01",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=20,unclaimed_cpus=12,total_memory=64000,claimed_memory=40000,unclaimed_memory=24000,total_loadavg=25.0,claimed_loadavg=12.5,unclaimed_loadavg=12.5,total_slots=4,claimed_busy_slots=3,unclaimed_idle_slots=1,querytime=1730910400,destination_id="pulsar_eu01",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=5,unclaimed_cpus=27,total_memory=64000,claimed_memory=10000,unclaimed_memory=54000,total_loadavg=4.0,claimed_loadavg=2.0,unclaimed_loadavg=2.0,total_slots=4,claimed_busy_slots=1,unclaimed_idle_slots=3,querytime=1730910500,destination_id="pulsar_asia01",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=64,claimed_cpus=50,unclaimed_cpus=14,total_memory=128000,claimed_memory=100000,unclaimed_memory=28000,total_loadavg=45.0,claimed_loadavg=22.5,unclaimed_loadavg=22.5,total_slots=8,claimed_busy_slots=6,unclaimed_idle_slots=2,querytime=1730910600,destination_id="pulsar_fr",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=15,unclaimed_cpus=17,total_memory=64000,claimed_memory=30000,unclaimed_memory=34000,total_loadavg=10.5,claimed_loadavg=5.5,unclaimed_loadavg=5.0,total_slots=4,claimed_busy_slots=2,unclaimed_idle_slots=2,querytime=1730910700,destination_id="pulsar_fr01_tpv",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=8,unclaimed_cpus=24,total_memory=64000,claimed_memory=16000,unclaimed_memory=48000,total_loadavg=8.0,claimed_loadavg=2.0,unclaimed_loadavg=6.0,total_slots=4,claimed_busy_slots=1,unclaimed_idle_slots=3,querytime=1730910800,destination_id="pulsar_de",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=16,claimed_cpus=12,unclaimed_cpus=4,total_memory=32000,claimed_memory=24000,unclaimed_memory=8000,total_loadavg=12.0,claimed_loadavg=8.0,unclaimed_loadavg=4.0,total_slots=2,claimed_busy_slots=1,unclaimed_idle_slots=1,querytime=1730910900,destination_id="pulsar_in",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=10,unclaimed_cpus=22,total_memory=64000,claimed_memory=20000,unclaimed_memory=44000,total_loadavg=15.0,claimed_loadavg=7.5,unclaimed_loadavg=7.5,total_slots=4,claimed_busy_slots=2,unclaimed_idle_slots=2,querytime=1730911000,destination_id="pulsar_cz01_tpv",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=32,claimed_cpus=5,unclaimed_cpus=27,total_memory=64000,claimed_memory=10000,unclaimed_memory=54000,total_loadavg=4.0,claimed_loadavg=2.0,unclaimed_loadavg=2.0,total_slots=4,claimed_busy_slots=1,unclaimed_idle_slots=3,querytime=1730911100,destination_id="pulsar_sk01_tpv",destination_status="online"
INSERT htcondor_cluster_usage,classad=machine total_detected_cpus=64,claimed_cpus=45,unclaimed_cpus=19,total_memory=128000,claimed_memory=90000,unclaimed_memory=38000,total_loadavg=40.0,claimed_loadavg=20.0,unclaimed_loadavg=20.0,total_slots=8,claimed_busy_slots=6,unclaimed_idle_slots=2,querytime=1730911200,destination_id="pulsar_uk",destination_status="online"

-- queue_by_destination
INSERT queue_by_destination,destination_id=condor_tpv,state=queued count=8
INSERT queue_by_destination,destination_id=condor_tpv,state=running count=4
INSERT queue_by_destination,destination_id=condor_us,state=queued count=12
INSERT queue_by_destination,destination_id=condor_us,state=running count=8
INSERT queue_by_destination,destination_id=pulsar_be01,state=queued count=5
INSERT queue_by_destination,destination_id=pulsar_be01,state=running count=5
INSERT queue_by_destination,destination_id=pulsar_us01,state=queued count=6
INSERT queue_by_destination,destination_id=pulsar_us01,state=running count=6
INSERT queue_by_destination,destination_id=pulsar_eu01,state=queued count=10
INSERT queue_by_destination,destination_id=pulsar_eu01,state=running count=3
INSERT queue_by_destination,destination_id=pulsar_asia01,state=queued count=2
INSERT queue_by_destination,destination_id=pulsar_asia01,state=running count=8
INSERT queue_by_destination,destination_id=pulsar_fr,state=queued count=4
INSERT queue_by_destination,destination_id=pulsar_fr,state=running count=10
INSERT queue_by_destination,destination_id=pulsar_fr01_tpv,state=queued count=8
INSERT queue_by_destination,destination_id=pulsar_fr01_tpv,state=running count=6
INSERT queue_by_destination,destination_id=pulsar_de,state=queued count=5
INSERT queue_by_destination,destination_id=pulsar_de,state=running count=5
INSERT queue_by_destination,destination_id=pulsar_in,state=queued count=6
INSERT queue_by_destination,destination_id=pulsar_in,state=running count=4
INSERT queue_by_destination,destination_id=pulsar_cz01_tpv,state=queued count=3
INSERT queue_by_destination,destination_id=pulsar_cz01_tpv,state=running count=2
INSERT queue_by_destination,destination_id=pulsar_sk01_tpv,state=queued count=10
INSERT queue_by_destination,destination_id=pulsar_sk01_tpv,state=running count=5
INSERT queue_by_destination,destination_id=pulsar_uk,state=queued count=7
INSERT queue_by_destination,destination_id=pulsar_uk,state=running count=8


-- destination-queue-run-time
INSERT destination-queue-run-time,destination_id=condor_tpv,tool_id=trinity count=5,avg_queue=4.0,min_queue=2,median_queue=3.5,perc_95_queue=7,perc_99_queue=8,max_queue=10,avg_run=2400,min_run=200,median_run=1800,perc_95_run=4000,perc_99_run=4500,max_run=5000
INSERT destination-queue-run-time,destination_id=condor_us,tool_id=spades count=10,avg_queue=15.0,min_queue=10,median_queue=12.0,perc_95_queue=25,perc_99_queue=30,max_queue=35,avg_run=7200,min_run=400,median_run=5000,perc_95_run=15000,perc_99_run=16000,max_run=18000
INSERT destination-queue-run-time,destination_id=pulsar_be01,tool_id=bwa count=3,avg_queue=3.5,min_queue=2,median_queue=3.0,perc_95_queue=6,perc_99_queue=7,max_queue=8,avg_run=3600,min_run=300,median_run=3000,perc_95_run=8000,perc_99_run=9000,max_run=10000
INSERT destination-queue-run-time,destination_id=pulsar_us01,tool_id=hisat2 count=12,avg_queue=6.5,min_queue=5,median_queue=6.0,perc_95_queue=15,perc_99_queue=20,max_queue=25,avg_run=5400,min_run=500,median_run=5000,perc_95_run=15000,perc_99_run=16000,max_run=18000
INSERT destination-queue-run-time,destination_id=pulsar_eu01,tool_id=bowtie2 count=8,avg_queue=10.5,min_queue=5,median_queue=8.0,perc_95_queue=15,perc_99_queue=20,max_queue=30,avg_run=7200,min_run=600,median_run=7000,perc_95_run=20000,perc_99_run=22000,max_run=25000
INSERT destination-queue-run-time,destination_id=pulsar_asia01,tool_id=blast count=20,avg_queue=8.0,min_queue=3,median_queue=7.0,perc_95_queue=12,perc_99_queue=15,max_queue=20,avg_run=3600,min_run=300,median_run=3000,perc_95_run=10000,perc_99_run=12000,max_run=15000
INSERT destination-queue-run-time,destination_id=pulsar_fr,tool_id=bwa count=8,avg_queue=5.5,min_queue=3,median_queue=5.0,perc_95_queue=10,perc_99_queue=12,max_queue=15,avg_run=3600,min_run=600,median_run=3000,perc_95_run=8000,perc_99_run=9000,max_run=10000
INSERT destination-queue-run-time,destination_id=pulsar_fr01_tpv,tool_id=hisat2 count=12,avg_queue=7.5,min_queue=5,median_queue=7.0,perc_95_queue=12,perc_99_queue=15,max_queue=20,avg_run=5400,min_run=500,median_run=5000,perc_95_run=15000,perc_99_run=16000,max_run=18000
INSERT destination-queue-run-time,destination_id=pulsar_de,tool_id=bowtie2 count=10,avg_queue=5.0,min_queue=2,median_queue=4.0,perc_95_queue=8,perc_99_queue=10,max_queue=12,avg_run=2400,min_run=300,median_run=2000,perc_95_run=4000,perc_99_run=4500,max_run=5000
INSERT destination-queue-run-time,destination_id=pulsar_in,tool_id=trinity count=6,avg_queue=6.5,min_queue=4,median_queue=6.0,perc_95_queue=10,perc_99_queue=12,max_queue=14,avg_run=3600,min_run=600,median_run=3000,perc_95_run=9000,perc_99_run=10000,max_run=11000
INSERT destination-queue-run-time,destination_id=pulsar_cz01_tpv,tool_id=spades count=5,avg_queue=4.0,min_queue=2,median_queue=3.5,perc_95_queue=6,perc_99_queue=7,max_queue=8,avg_run=3600,min_run=300,median_run=3000,perc_95_run=8000,perc_99_run=9000,max_run=10000
INSERT destination-queue-run-time,destination_id=pulsar_sk01_tpv,tool_id=blast count=7,avg_queue=8.0,min_queue=3,median_queue=7.0,perc_95_queue=12,perc_99_queue=15,max_queue=20,avg_run=3600,min_run=300,median_run=3000,perc_95_run=10000,perc_99_run=12000,max_run=15000
INSERT destination-queue-run-time,destination_id=pulsar_uk,tool_id=hisat2 count=15,avg_queue=15.5,min_queue=10,median_queue=14.0,perc_95_queue=20,perc_99_queue=25,max_queue=30,avg_run=5400,min_run=300,median_run=5000,perc_95_run=10500,perc_99_run=12000,max_run=13000
