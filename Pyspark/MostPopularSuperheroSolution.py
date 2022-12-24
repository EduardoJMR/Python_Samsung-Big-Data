from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

from sys import argv
#
# Encuentra el superheroe con mas conexiones.
#

if __name__ == "__main__": 

  # Crea una SparkSession que use todo los cores de la maquina local
  spark = (SparkSession.
    builder.
    appName("MostPopularSuperhero").
    master("local[*]").
    getOrCreate() )

  spark.sparkContext.setLogLevel("ERROR")

  #
  # Crear el DataFrame leyendo el fichero
  #
  lines = spark.read.text( "/user/training/data/" + argv[1] )

  #
  # Por cada heroe calcula la suma
  # de todos lo heroes con los que
  # aparece en una pelicula.
  #
  # Es decir, la suma de todas sus
  # conexiones.
  #
  connections = (lines.
    withColumn("id", split(col("value"), " ")[0]).
    withColumn("connections", size(split(col("value"), " ")) - 1).
    groupBy("id").
    agg(sum("connections").alias("connections")) )

  #
  # Obten el heroe con mas conexiones.
  #
  # Despues de la ejecucion:
  #   mostPoular[0]: id
  #   mostPoular[1]: numero de conexiones
  #
  mostPopular = (connections.
    sort( col("connections").desc() ).
    first() )

  #
  # Esquema para el DataFrame que asocia
  # un id al nombre del heroe.
  #
  superHeroNamesSchema = (StructType().
    add("id", IntegerType(), nullable = True).
    add("name", StringType(), nullable = True) )

  #
  # Lee el DataFrame con los nombres
  #
  names = (spark.read.
    schema(superHeroNamesSchema).
    option("sep", " ").
    csv("data/Marvel-names.txt") )

  #
  # Busca en el DataFrame name el Row
  # que contiene como primer elemento
  # el id del heroe con mas conexiones.
  #
  mostPopularName = (names.
    filter( col("id") == mostPopular[0] ).
    select("name").
    first() )

  output = "{0} es el heroe mas popular con {1} conexiones."
  print( output.format( mostPopularName[0], mostPopular[1] ) )

  spark.stop
