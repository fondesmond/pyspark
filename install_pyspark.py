###  Install Spark

!apt-get update
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
!wget -q http://archive.apache.org/dist/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz
!tar xf spark-2.3.1-bin-hadoop2.7.tgz
!pip install -q findspark
###  Command took 32.31 seconds -- by fondesmond@yahoo.co.uk at 18/04/2020, 23:43:14 on v-defona


import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.3.1-bin-hadoop2.7"
###  Command took 0.03 seconds -- by fondesmond@yahoo.co.uk at 18/04/2020, 23:43:14 on v-defona

!ls
###  List fs
###  Command took 0.04 seconds -- by fondesmond@yahoo.co.uk at 18/04/2020, 23:43:14 on v-defona

import findspark
from pyspark import SparkContext

sc = SparkContext.getOrCreate()
6
sc
Out[8]: 
###  Command took 0.06 seconds -- by fondesmond@yahoo.co.uk at 18/04/2020, 23:43:14 on v-defona

import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate() 

spark
Out[9]: