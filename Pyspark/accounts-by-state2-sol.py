import sys

from pyspark.sql import SparkSession

def processState( state ):
  outdir = "/devsh_loudacre/accounts_by_state/" + state

  accountsDF. \
   filter( accountsDF.state == state ). \
   write.mode( "overwrite" ). \
   save( outdir ) 

if __name__ == "__main__":

  spark = SparkSession.builder.getOrCreate()
  spark.sparkContext.setLogLevel("WARN")
  
  accountsDF = spark.read.table("devsh.accounts").persist()
  statesRow = ( accountsDF.
    select("state").
    distinct().
    collect() )
  states = map( lambda r: r[0], statesRow)

  for s in states:
    print (s)
    processState( s )

  spark.stop()
