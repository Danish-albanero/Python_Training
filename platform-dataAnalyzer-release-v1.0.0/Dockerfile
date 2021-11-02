FROM python:3.6

SHELL ["/bin/bash", "-c"] 

#setup java
RUN apt-get update
RUN apt-get install zip unzip -y
RUN curl -s "https://get.sdkman.io" | bash
RUN source "$HOME/.sdkman/bin/sdkman-init.sh" && sdk install java 8.0.265-open -y
SHELL ["/bin/sh", "-c"] 
ENV JAVA_HOME=/root/.sdkman/candidates/java/current

#application code setup
WORKDIR /app

# setup pyspark dependencies
RUN wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/2.7.4/hadoop-aws-2.7.4.jar
RUN wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk/1.7.4.2/aws-java-sdk-1.7.4.2.jar
RUN wget https://repo1.maven.org/maven2/com/amazon/deequ/deequ/1.0.3/deequ-1.0.3.jar
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.14.jre6.jar -O postgresql-42.2.14.jar
RUN wget https://www.datanucleus.org/downloads/maven2/oracle/ojdbc6/11.2.0.3/ojdbc6-11.2.0.3.jar -O ojdbc6.jar

COPY requirements.txt /app

RUN PYSPARK_HADOOP_VERSION=2.7.4 pip install -r requirements.txt

COPY . /app

EXPOSE 3082

ENTRYPOINT [ "gunicorn" ]

CMD ["--bind", "0.0.0.0:3082", "wsgi:app"]