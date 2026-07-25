# Week 6 Assignment Report
## Apache Spark Architecture and Data Processing

**Intern:** Gaurav Gaikwad  
**Internship:** Celebal Technologies – Data Engineering Internship  
**Week:** 6  
**Technology:** Apache Spark (PySpark)

---

# Objective

The objective of this assignment is to understand the architecture of Apache Spark and perform data processing using PySpark DataFrames. The assignment focuses on distributed computing concepts, Spark architecture, DataFrame transformations, actions, lazy evaluation, execution plans, and efficient data storage techniques.

---

# Problem Statement

Modern organizations generate massive amounts of structured and unstructured data that cannot be processed efficiently using traditional single-machine systems. Apache Spark provides a distributed computing framework capable of processing large datasets efficiently through in-memory computation and parallel execution.

The goal of this assignment is to explore Spark Architecture, understand its execution model, and implement various DataFrame operations while studying optimization techniques such as Lazy Evaluation, DAG execution, and Predicate Pushdown.

---

# Dataset

**Dataset Used:** Sample Superstore Dataset

The dataset contains sales transactions with information including:

- Order Details
- Customer Information
- Product Information
- Region
- Sales
- Profit
- Discount
- Quantity

---

# Tasks Performed

The following operations were successfully performed:

- Created a Spark Session
- Loaded CSV data into a Spark DataFrame
- Displayed sample records
- Printed DataFrame schema
- Renamed selected columns
- Changed data types using casting
- Added a new calculated column
- Filtered records using conditions
- Selected required columns
- Checked for null values
- Demonstrated Spark Transformations and Actions
- Explained Spark Execution Plan
- Demonstrated Lazy Evaluation
- Compared CSV and Parquet storage concepts
- Answered theoretical questions on Spark Architecture and optimization techniques

---

# Key Concepts Learned

During this assignment, the following Apache Spark concepts were explored:

- Spark Architecture
- Driver Program
- Cluster Manager
- Executors
- SparkSession
- DataFrame API
- Transformations
- Actions
- Lazy Evaluation
- Directed Acyclic Graph (DAG)
- Catalyst Optimizer
- Predicate Pushdown
- CSV vs Parquet
- Fault Tolerance
- Distributed Data Processing

---

# Challenges Faced

While implementing the assignment, the following challenges were encountered:

- Parsing issues while reading the CSV dataset due to formatting inconsistencies.
- Windows environment required Hadoop configuration (`HADOOP_HOME` and `winutils.exe`) for writing CSV and Parquet files.
- Some theory questions used generic DataFrames and column names (for example `df_orders`, `status`, `amount`, `base_price`, and `priority`) that were not part of the provided Superstore dataset. These were answered as Spark syntax examples while practical implementation was demonstrated using the available dataset.

---

# Outcome

The assignment provided practical exposure to Apache Spark and distributed data processing. It demonstrated how Spark efficiently processes large datasets using in-memory computation, lazy evaluation, optimized execution plans, and fault tolerance mechanisms.

The practical implementation strengthened understanding of DataFrame operations, Spark architecture, distributed execution, and performance optimization techniques commonly used in modern Big Data applications.

---

# Conclusion

This assignment successfully demonstrated the implementation of Apache Spark using PySpark for scalable data processing. Practical tasks such as loading data, transforming datasets, filtering records, and analyzing execution plans were completed successfully. In addition, theoretical concepts including Spark Architecture, Driver and Executor roles, DAG, Lazy Evaluation, Predicate Pushdown, and DataFrame operations were studied in detail. Overall, this assignment enhanced both conceptual understanding and practical skills required for building efficient Big Data processing pipelines using Apache Spark.

---

# Tools and Technologies

- Apache Spark
- PySpark
- Python
- Jupyter Notebook
- Pandas
- CSV Dataset
- Apache Parquet (Concept)