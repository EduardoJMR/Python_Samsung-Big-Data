from pyspark.sql.functions import regexp_replace
from pyspark.sql.functions import col
from pyspark.sql.functions import month

spark.sql("CREATE DATABASE IF NOT EXISTS hr_db" )

(spark.read.
  parquet( "/data/hr_records_parquet_data/" ).
  withColumn( "phone_nbr",
    regexp_replace( col("phone_nbr"), "-", " " ) ).
  filter( month( col("date_of_birth") ) == 1 ).
  write.
  mode( "overwrite" ).
  option( "compression", "gzip" ).
  format( "parquet" ).
  saveAsTable( "hr_db.problem2" ) )

##################################################

df = spark.read.table( "hr_db.problem2" )

print( df.count() )
df.printSchema()
(df.
  select( "date_of_birth", "first_name", "last_name", "phone_nbr" ).
  orderBy( "phone_nbr" ).
  show(10, False) )
