from pyspark.sql.functions import regexp_replace
from pyspark.sql.functions import col

spark.sql("CREATE DATABASE IF NOT EXISTS hr_db" )

(spark.read.
  parquet( "/data/hr_records_parquet_data/" ).
  withColumn( "phone_number",
    regexp_replace( col("phone_nbr"), "-", "" ).cast("long") ).
  drop( "phone_nbr" ).
  write.
  mode( "overwrite" ).
  option( "compression", "gzip" ).
  format( "parquet" ).
  saveAsTable( "hr_db.problem2" ) )

##################################################

df = spark.read.table( "hr_db.problem2" )

df.printSchema()
(df.
  select( "first_name", "last_name", "phone_number" ).
  orderBy( "phone_number" ).
  show(5, False) )
