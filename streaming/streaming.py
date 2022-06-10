from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType, FloatType

spark = SparkSession \
    .builder \
    .appName("Structured_App_Demo") \
    .getOrCreate()

# po co komu security, klucz juz dawno zrotowany ;)
spark.conf.set("fs.azure.account.key.testquhqwdiuq.blob.core.windows.net",
               "dwg3C+KEGpBHTG1ME6/QIzXNY3VtShHytaDH28kOCkw3ah+AsNXbg4jJ6usoymcXRZNsuro8v8KY+AStrwcJ9A==")

schema = StructType([
    StructField("Username", StringType(), True),
    StructField("Identifier", IntegerType(), True),
    StructField("Firstname", StringType(), True),
    StructField("Lastname", StringType(), True)
])

df = spark.readStream \
    .format("csv") \
    .option("header", "true") \
    .schema(schema) \
    .option("sep", ";") \
    .load("wasbs://orkuz@testquhqwdiuq.blob.core.windows.net/spark_input")

df.printSchema()

df.writeStream.format("console").outputMode("append").start().awaitTermination()
