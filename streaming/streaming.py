from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, BooleanType, FloatType

spark = SparkSession \
    .builder \
    .appName("Structured_App_Demo") \
    .getOrCreate()

spark.conf.set("fs.azure.account.key.testquhqwdiuq.blob.core.windows.net",
               "08yTLzJw8v/MYy3oYh4PU1E64oEj3pzZLFAOwy1kfk+mlUnUN2LOmm7B+nk4TsDoSWOHxNgzgSqO+AStysirXQ==")


schema = StructType([
    StructField("Username", StringType(), True),
    StructField("Identifier", IntegerType(), True),
    StructField("Firstname", StringType(), True),
    StructField("Lastname", StringType(), True)
])

df = spark.readStream \
    .format("csv") \
    .option("header","true")\
    .schema(schema)\
    .option("sep", ";")\
    .load("wasbs://husky@testquhqwdiuq.blob.core.windows.net/spark_input")

df.printSchema()

df.writeStream.format("console").outputMode("append").start().awaitTermination()

# df.writeStream \
#     .format("parquet") \
#     .outputMode("append") \
#     .option("checkpointLocation", "/tmp/delta/events/_checkpoints/") \
#     .start("path/to/destination/dir")
