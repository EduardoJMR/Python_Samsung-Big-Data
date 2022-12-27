# Python_Spark_Samsung-Big-Data

## HDFS

![What is HDFS?](https://www.researchgate.net/publication/348387085/figure/fig4/AS:981518453309440@1611023643650/The-overview-of-the-Hadoop-Distributed-File-System-HDFS.ppm)

* Write Once, Read Many times (WORM).
* Divide files into big blocks and distribute across the cluster.
* Store multiple replicas of each block for reliability.
* Programs can ask "where do the pieces of my file live?”.

## HDFS Components

### NameNode
* Is the master service of HDFS. 
* Determines and maintains how the chunks of data are distributed across the DataNodes. 
### DataNode
* Stores the chunks of data, and is responsible for replicating the chunks across other DataNodes.
* The NameNode(master node) and DataNodes(worker nodes) are daemons running in a Java virtual machine.
### The HDFS NameNodeis a single point of failure:
* The entire cluster is unavailable if the NameNode:
* Fails or becomes unreachable.
* Is stopped to perform maintenance.
### NameNodeHA:
* Uses a redundant NameNode
* Is configured in an Active/Standby configuration
* Enables fast failover in response to NameNodefailure
* Permits administrator-initiated failover for maintenance
* Is configured by Cloudera Manager
## HDFS Architecture
* The NameNode(master node) and DataNodes(worker nodes) are daemons running in a Java virtual machine.

## YARN Resource Management

* Yet Another Resource Negotiator
* Architectural center of Enterprise Hadoop
* Provides centralized resource management and job scheduling across multiple types of processing workloads
* Enables multi tenancy

### YARN Architectural Components 
#### Resource Manager
* Global resource scheduler
* Hierarchical queues
#### Node Manager
* Per-machine agent
* Manages the life-cycle of container
* Container resource monitoring
#### Application Master
* Per-application
* Manages application scheduling and task execution
* E.g. MapReduce Application Master

## Resilient Distributed Datasets (RDDs)

#### RDDs are part of core Spark
* Resilient Distributed Dataset (RDD)
* Resilient: if data in memory is lost, it can be recreated
* Distributed: Processed across the cluster
* Dataset: Initial data can come from a source such as a file, or it can be created programmatically
### All Transformations are Lazy
#### Spark doesn't immediately compute results
* Transformations stored as a graph (DAG) from a base RDD
* Consider an RDD to be a set of operations
* It's not really a container for specific data
#### The DAG is executed when an action occurs
* When it needs to provide data
#### Allows Spark to:
* Optimize required calculations (we'll view this soon)
* Efficiently recover RDDs on node failure (more on this later)
#### Fault Tolerance
#### Spark tracks transformations that create an RDD
* Lineage: The series of transformations producing an RDD
#### A lost partition can be rebuilt from its lineage
* Efficient, and adds little overhead to normal operation

## DataFrames and Datasets

#### DataFrames and Datasets are the primary representation of data in Spark. 
#### DataFrames represent structured data in a tabular form.
* DataFrames model data similar to tables in an RDBMS. 
* DataFrames consist of a collection of loosely typed Row objects. 
* Rows are organized into columns described by a schema.
#### Datasets represent data as a collection of objects of a specified type.
* Datasets are strongly-typed—type checking is enforced at compile time rather than run time.
* An associated schema maps object properties to a table-like structure of rows and columns.
* Datasets are only defined in Scala and Java.
* DataFrameis an alias for Dataset[Row]—Datasets containing Row objects.
* DataFrameOperaMons: Transformations
* Transformations create a new DataFrame based on an existing one
* Transformations create a new DataFrame based on an existing one
#### Transformations do not return any values or data to the driver
* Data remains distributed across the application’s executors
#### DataFrames are immutable
* Data in a DataFrame is never modified
* Use transformations to create a new DataFrame with the data you need

## Apache Hive

#### SQL Semantic Layer on Hadoop
#### “De facto SQL Interface” for Hadoop
#### Originally developed by Facebook
#### Original Appeal
* Schema on Read
* SQL to Map Reduce (Reduce complexity of Map Reduce)
* Familiar Programming Context with SQL
#### It is a data warehouse system for Hadoop
#### It maintains metadata information about your big data stored on HDFS
#### Big data can be queried as tables
#### It performs SQL-like operations on the data using a scripting language called HiveQL

### Distributed Processing Challenges
#### Shuffle
##### SELECT COUNT(*) FROM WHERE GROUP BY ORDER BY
#### Skew
##### SELECT COUNT(*) FROM WHERE GROUP BY ORDER BY
#### OrderDistributed
##### SELECT COUNT(*) FROM WHERE GROUP BY ORDER BY

## Message Processing with Apache Kafka

#### Apache Kafka is a distributed commit log service
* Widely used for data ingest
* Conceptually similar to a publish-subscribe messaging system 
* Offers scalability, performance, reliability, and flexibility
#### Originally created at LinkedIn, now an open source Apache project
* Donated to the Apache Software Foundation in 2011
* Graduated from the Apache Incubator in 2012
* Supported by Cloudera for production use with CDH in 2015
### Key Terminology
#### Message
* A single data record passed by Kafka
* Messages in Kafka are variable-size byte arrays
* There is no explicit limit on message size
* Kafka retains all messages for a defined time period and/or total size
#### Topic
* There is no explicit limit on the number of topics
* A topic can be created explicitly or simply by publishing to the topic
* A named log or feed of messages within Kafka
#### Producer
* Producers publish messages to Kafka topics
* A program that writes messages to Kafka
#### Consumer
* A program that reads messages from Kafka
* A consumer reads messages that were published to Kafka topics
* Consumer actions do not affect other consumers
* They can come and go without impact on the cluster or other consumers
#### Kafka Clusters
* A Kafka cluster consists of one or more brokers—servers running the Kafka broker daemon
* Kafka depends on the Apache ZooKeeper service for coordination
### Zookeeper
#### Kafka depends on the ZooKeeper service for coordination
* Typically running three or five ZooKeeper instances
#### Apache ZooKeeper is a coordination service for distributed applications 
#### Kafka uses ZooKeeper to keep track of brokers running in the cluster 
#### Kafka uses ZooKeeper to detect the addition or removal of consumers
### Kafka Brokers
#### Brokers are the fundamental daemons that make up a Kafka cluster
#### A broker fully stores a topic partition on disk, with caching in memory
#### A single broker can reasonably host 1000 topic partitions
#### One broker is elected controller of the cluster (for assignment of topic partitions to brokers, and so on)
#### Each broker daemon runs in its own JVM
##### A single machine can run multiple broker daemons
### Topic Replication
#### At topic creation, a topic can be set with a replication count
* Doing so is recommended, as it provides fault tolerance
#### Each broker can act as a leader for some topic partitions and a follower for others
* Followers passively replicate the leader
* If the leader fails, a follower will automatically become the new leader
### Messages are Replicated
#### Configure the producer with a list of one or more brokers
#### The producer asks the first available broker for the leader of the desired topic partition
#### The producer then sends the message to the leader
* The leader writes the message to its local log
* Each follower then writes the message to its own log
* After acknowledgements from followers, the message is committed
