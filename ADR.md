[https://docs.google.com/open?id=38929ddfj_989adfasdf


### Decision 
* Decide to use MongoDB for Cloud DB
### 
### Positive Consequences
* It is easy to install, use and schema-less database.
* Due to it is the ability of a schema-less database, the code which we create defines the schema.
* Data is stored in Binary JSON format, which is key-value pair, no joins complexity is needed.
* It uses RAM to store data; this makes faster access to the data.
* It can be used for load balancing.
* It supports ACID (atomicity, consistency, isolation, and durability) property for a database transaction.
* It supports replication; if the primary server goes down during transaction, then the secondary server handles the transaction without human interaction.
* It is cost-effective because it reduces cost on hardware and storage.
* It can save a lot of data which will help in faster query processing.
* Data is stored across the cluster nodes, so there will be no single point of failure in the database server.
### 
### Negative Consequences
* Data size in MongoDB is typically higher due to e.g. each document has field names stored it
* Less flexibity with querying (e.g. no JOINs)
* No support for transactions - certain atomic operations are supported, at a single document level
* At the moment Map/Reduce (e.g. to do aggregations/data analysis) is OK, but not blisteringly fast. So if that's required, something like Hadoop may need to be added into the mix
* Less up to date information available/fast evolving product
