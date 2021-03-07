from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

from metis_services.test_app import print_context

args = {"owner": "airflow", "provide_context": True}

dag_for_test = DAG(
    dag_id="metis_app_test",
    schedule_interval=None,
    start_date=datetime(year=2021, month=2, day=20, hour=4, minute=0, second=0),
    concurrency=4,
    max_active_runs=1,
    default_args=args,
)

start_task = BashOperator(
    task_id="start_task", bash_command="echo testing app", dag=dag_for_test,
)


testing_script = PythonOperator(
    task_id="print_the_context",
    python_callable=print_context,
    op_kwargs={"data_path": "some_data_path",},
    dag=dag_for_test,
)

start_task >> testing_script
