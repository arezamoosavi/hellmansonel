FROM python:3.7-slim-stretch

RUN apt-get update -y && apt-get install -y libzbar-dev bash gcc git libc-dev curl wget vim nano \
    && apt-get install -y ranger caca-utils highlight atool w3m poppler-utils mediainfo \
    && apt-get install -y iputils-ping telnet openssh-client net-tools \
    man unzip vim-tiny bc openssh-server thrift-compiler netcat sudo \
    && apt-get install -y build-essential \
    && apt-get autoremove -y \
    && apt-get clean

# Install OpenJDK 8
RUN mkdir -p /usr/share/man/man1mkdir -p /usr/share/man/man1 && \
    apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$PATH:$JAVA_HOME/bin
RUN echo $JAVA_HOME

# install spark
RUN wget --no-verbose https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz && \
    tar -xzvf spark-3.0.1-bin-hadoop3.2.tgz && \
    mv spark-3.0.1-bin-hadoop3.2 /opt/spark && \
    rm -rf spark-3.0.1-bin-hadoop3.2.tgz

ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin
ENV PATH=$PATH:$SPARK_HOME/sbin
ENV PYTHONPATH=$SPARK_HOME/python3:$SPARK_HOME/python3/lib/py4j-0.10.7-src.zip:$PYTHONPATH
RUN mkdir -p /opt/spark/history

# install scala
# RUN wget --no-verbose https://downloads.lightbend.com/scala/2.12.10/scala-2.12.10.tgz && \
#     tar -xzvf scala-2.12.10.tgz && \
#     mv scala-2.12.10 /opt/scala
# ENV SCALA_HOME=/opt/scala
# ENV PATH=$PATH:$SCALA_HOME/bin

#Project
COPY dockers/airflow/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m airflow && echo "airflow:airflow" | chpasswd && adduser airflow sudo
RUN chown airflow /usr/local

RUN mkdir -p /opt/airflow/dags
RUN chown airflow /opt/airflow

COPY ./dags ./opt/airflow/dags
RUN chmod -R a+rwx /opt/airflow
RUN chmod -R a+rwx /opt/spark/history

COPY dockers/airflow/airflow.cfg /opt/airflow/airflow.cfg

COPY dockers/airflow/run.sh /run.sh
RUN chmod a+rwx /run.sh

WORKDIR /opt/airflow
USER airflow
