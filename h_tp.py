# Databricks notebook source
import csv
import boto3
import datetime
import pandas as pd

from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.types import StructType, StructField, StringType

from datetime import datetime
from unidecode import unidecode
from connections_mit import Oracle, Redshift
import json
import psycopg2 

from connections_mit import Oracle, Redshift, Spark
from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql.functions import col, to_date, when, udf, struct, get_json_object, lit, monotonically_increasing_id
from pyspark.sql.types import IntegerType, ArrayType, MapType, StringType, StructType
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", 100)