#!/bin/sh


set -o errexit
set -o nounset

start-history-server.sh
echo "History server is sarting ...."
sleep 2
echo "Master is sarting ...."
start-master.sh

sleep 1
echo "Master started at port 8080 ...."

echo "worker is sarting ...."

start-worker.sh spark://airflow:7077

sleep 1
echo "worker started at port 8081 ...."

airflow initdb

sleep 2

echo "airflow app started ...."

airflow webserver -p 8080 & sleep 2 & airflow scheduler
