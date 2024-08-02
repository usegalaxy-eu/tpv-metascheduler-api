#!/bin/bash


# This script is used to monitor the condor jobs status in the cluster including the compute resources, job submit time to the queue, job start time, job description, etc.

condor_q -global -autoformat GlobalJobId JobStatus Cmd RemoteHost RequestCpus RequestMemory QDate JobStartDate JobDescription | awk '
BEGIN {
  status["0"] = "Unexpanded"; status["1"] = "Idle"; status["2"] = "Running";
  status["3"] = "Removed"; status["4"] = "Completed"; status["5"] = "Held";
  status["6"] = "Submission_err";
}
{
  if ($0 == "All queues are empty") {
    # If the output indicates that all queues are empty, print a message and exit
    print "condor_queued_jobs_status,schedd=All,clusterid=0 jobstatus=\"Empty\",cmd=\"\",remotehost=\"\",requestcpus=0,requestmemory=0,qdate=\"1970-01-01 00:00:00\",jobstartdate=\"1970-01-01 00:00:00\",jobdescription=\"\"";
    exit;
  }

  # Split the global job ID into components
  split($1, globalID, "#");
  split(globalID[2], condorID, "#");

  # Format dates if they are not undefined
  if ($8 != "undefined") $8 = strftime("%Y-%m-%d %H:%M:%S", $8);
  if ($7 != "undefined") $7 = strftime("%Y-%m-%d %H:%M:%S", $7);

  # Assign default values if needed
  if ($5 == "") $5 = 0;  # Default for requestcpus
  if ($6 == "") $6 = 0;  # Default for requestmemory

  # Combine job description fields
  jobdesc = $9;
  for (i = 10; i <= NF; i++) {
    jobdesc = jobdesc "_" $i;
  }

  # Print the formatted output
  printf "condor_queued_jobs_status,schedd=%s,clusterid=%s jobstatus=\"%s\",cmd=\"%s\",remotehost=\"%s\",requestcpus=%s,requestmemory=%s,qdate=\"%s\",jobstartdate=\"%s\",jobdescription=\"%s\"\n",
    globalID[1], condorID[1], status[$2], $3, $4, $5, $6, $7, $8, jobdesc;
}'



# condor_q -global -autoformat GlobalJobId JobStatus Cmd RemoteHost RequestCpus RequestMemory QDate JobStartDate JobDescription | awk '{
#   if ($8 != "undefined") $8 = strftime("%Y-%m-%d %H:%M:%S", $8);
#   split($1,globalID,"#");
#   split(globalID[2],condorID,"#");
#   status["0"]="Unexpanded"; status["1"]="Idle"; status["2"]="Running"; status["3"]="Removed"; status["4"]="Completed"; status["5"]="Held"; status["6"]="Submission_err";

#   jobdesc = $9;

#   for (i = 10; i <= NF; i++) {
#     jobdesc = jobdesc "_" $i;
#   }

#   printf "condor_queued_jobs_status,schedd=%s,clusterid=%s jobstatus=\"%s\",cmd=\"%s\",remotehost=\"%s\",requestcpus=%s,requestmemory=%s,qdate=\"%s\",jobstartdate=\"%s\",jobdescription=\"%s\"\n", globalID[1], condorID[1], status[$2], $3, $4, $5, $6, strftime("%Y-%m-%d %H:%M:%S", $7), $8, jobdesc
# }'
