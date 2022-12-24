from pyspark.sql.functions import col

(spark.read.
  option( "header", True ).
  csv( "/data/WHO_data/population" ).
  na.
  drop( "any", subset=[ "Pop1", "Pop2", "Pop3"] ).
  write.
  mode( "overwrite" ).
  option( "compression", "uncompressed" ).
  parquet( "/output/problem3" ) )

##################################################


df = spark.read.parquet( "/output/problem3" )

print( df.count( ) )

(df.
  select( "Country", "Year", "Sex", "Frmat", "Pop1", "Pop2", "Pop3", "Pop8", "Pop10"  ).  
  orderBy( "Country", "Year", "Sex" ).
  show(8, False) )

