(spark.read.
  option( "header", True).
  csv( "/data/CVD_mortality_rates_csv_data/" ).
  filter( "Gender = 'Female' AND Year != '2017'" ).
  select( "Year", "Gender", "Lower CI", "Upper CI" ).
  write.
  mode( "overwrite" ).
  option( "compression", "lzo" ).
  orc( "/output/problem1" ) )

##################################################

df = (spark.read.
  orc( "/output/problem1" ).
  orderBy( "Lower CI", "Upper CI", "Year" ) )

print( df.count() )
df.printSchema()

df.show(7, False) 
