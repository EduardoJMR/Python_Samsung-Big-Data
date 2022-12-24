from pyspark.sql.functions import col

(spark.read.
  parquet( "/data/sales_records_parquet_data/" ).
  withColumn( "units_sold", col("units_sold").cast("int") ).
  filter( "country = 'Spain'" ).
  createOrReplaceTempView( "temp_view" ) )

(spark.sql(
  """
  SELECT item_type, sum( units_sold) total_sold
  FROM temp_view
  GROUP By item_type
  """).
  coalesce( 1 ).
  write.
  mode( "overwrite" ).
  option( "compression", "gzip" ).
  option( "header", "True" ).
  option( "sep", ":" ).
  csv( "/output/problem4/" ) )

##################################################

df = (spark.read.
  option( "sep", ":").
  option( "header", True ).
  option( "inferSchema", True ).
  csv( "/output/problem4/" ).
  orderBy( "item_type" ) )

df.printSchema()
df.show(12, False )
