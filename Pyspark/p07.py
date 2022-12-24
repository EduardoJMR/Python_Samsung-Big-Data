from pyspark.sql.functions import col

(spark.read.
  option( "header", True ).
  csv( "/data/WHO_data/population" ).
  na.
  fill( "N/K" ).
  write.
  mode( "overwrite" ).
  option( "compression", "uncompressed" ).
  parquet( "/output/problem3" ) )

##################################################

df = spark.read.parquet( "/output/problem3" )

print( df.filter( col("Pop3") == "N/K").count() )
print( df.filter( col("Pop8") == "N/K").count() )
print( df.filter( col("Pop10") == "N/K").count() )
  
(df.
  select( "Country", "Year", "Sex", "Frmat", "Pop1", "Pop2", "Pop3", "Pop8", "Pop10"  ).
  orderBy( "Country", "Year", "Sex" ).
  show(5, False) )
