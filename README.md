# hellmansonel
Spark jobs Scala- Airflow

## Building Spark App

for creating the project's jar file:

```bash
sbt clean assembly
```
Then move jar file to airflow dag folder:

```bash
sudo mv target/scala-2.12/*.jar dags/app_services/spark_pca.jar
```

## Running Airflow

for creating the container:
```bash
docker-compose up --build -d
```
to stop it
```bash
docker-compose down -v
```
## Usage

#### Airflow
```bash
http://localhost:8080
```

After seting airflow variables the dag could be run using local spark in airflow container!
