build-airflow:
	docker-compose up --build -d airflow

up-airflow:
	docker-compose up -d airflow

rm-airflow:
	docker-compose stop airflow
	docker-compose rm airflow

ex-airflow:
	docker-compose exec airflow bash

logs-airflow:
	docker-compose logs -f airflow

down:
	docker-compose down -v