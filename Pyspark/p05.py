(spark.read.
  option( "header", True).
  csv( "/data/CVD_mortality_rates_csv_data/" ).
  drop( "Year" ).
  write.
  mode( "overwrite" ).
  option( "compression", "lzo" ).
  orc( "/output/problem1" ) )

##################################################

df = (spark.read.
  orc( "/output/problem1" ).
  orderBy( "Lower CI", "Upper CI", "Numerator", "Denominator" ) )

df.printSchema()
(df.select(
  "Gender", "Age", "Indicator value",
  "Lower CI", "Upper CI", "Numerator",
  "Denominator" ).
  show(5, False) )
print( df.count() )
