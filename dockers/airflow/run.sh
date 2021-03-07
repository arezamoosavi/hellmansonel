#!/bin/sh


set -o errexit
set -o nounset

airflow initdb

sleep 2

echo "airflow app started ...."

airflow webserver -p 8080 & sleep 2 & airflow scheduler
