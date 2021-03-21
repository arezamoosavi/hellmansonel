from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

args = {"owner": "airflow", "provide_context": True}

dag = DAG(
    dag_id="spark_run_pca",
    schedule_interval=None,
    start_date=datetime(year=2021, month=2, day=20, hour=4, minute=0, second=0),
    concurrency=4,
    max_active_runs=1,
    default_args=args,
)

start_task = BashOperator(
    task_id="start_task", bash_command="echo spark_run_pca", dag=dag,
)

spark_run_pca = BashOperator(
    task_id="run_spark_validation_check_core_local",
    bash_command="""spark-submit --verbose \
        --master local {{var.value.airflow_home}}/dags/app_services/spark_pca.jar \
        {{var.value.airflow_home}}/dags/app_services/data/Cancer_Data""",
    dag=dag,
)

start_task >> spark_run_pca
