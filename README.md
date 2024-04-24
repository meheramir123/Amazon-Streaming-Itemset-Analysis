# Amazon-Streaming-Itemset-Analysis
This project aims to analyze a sampled dataset from Amazon using streaming data processing techniques and frequent itemset mining algorithms.
This repository hosts a streaming frequent itemset mining implementation using Apache Kafka. The system comprises several components, including:
**Frequent Itemset Mining with Apriori, PCY, and FP-Growth Algorithms**

### 1. Introduction
Frequent itemset mining is a crucial task in data mining and finds numerous applications, including market basket analysis, bioinformatics, and network traffic analysis. This document outlines the implementation of frequent itemset mining using Apriori, PCY, and FP-Growth algorithms. It also includes integration with MongoDB and preprocessing Amazon_meta.json file using Apache Kafka Producer and Consumer.


## Preprocessing

Before starting the frequent itemset mining, the data needs to be preprocessed. Preprocessing the Amazon_meta.json file involves cleaning and transforming the data into a suitable format for frequent itemset mining. Apache Kafka Producer and Consumer facilitate this preprocessing task efficiently.


### Features:

**1. Load the Sampled Amazon dataset:**

The Amazon dataset is loaded and read from `preprocessed_data.json`.
  
**2. Process the data to clean and format it for analysis, ensuring it is suitable for the streaming and frequent itemset mining process:**

The data is preprocessed to make it suitable for the streaming and frequent itemset mining process. This includes the following steps:
  
- **Normalization**: JSON data is transformed into a DataFrame.
- **Drop Unnecessary Columns**: Columns such as 'imageURL', 'imageURLHighRes', 'tech1', 'tech2', 'description', and 'similar' are dropped.
- **Convert Lists to Strings**: Columns like 'feature', 'also_buy', 'also_viewed', and 'categories' are converted from lists to strings.

## Streaming Pipeline Setup

Once the data is preprocessed, the streaming pipeline is set up.


### Features:

**Apriori Consumer:**

This consumer implements the Apriori algorithm.T he Apriori algorithm is a classical algorithm used for frequent itemset mining. It uses a breadth-first search strategy and a candidate generation process to compute the support of itemsets. The steps involved are:
1. **Generate Candidate Itemsets**
2. **Prune Candidate Itemsets**
3. **Calculate Support**
4. **Repeat Steps 1-3 until no more frequent itemsets can be found** 

**PCY Consumer:**

This consumer implements the PCY algorithm. The PCY algorithm improves upon the Apriori algorithm by using a hash-based technique to prune candidate itemsets efficiently. It includes the following steps:
1. **Hashing and Counting**
2. **Filtering**
3. **Candidate Generation**
4. **Support Counting**


**FP-Growth Consumer:**

This consumer implements the FP-Growth algorithm. The FP-Growth algorithm is another method for frequent itemset mining, which uses a divide-and-conquer strategy to find frequent itemsets. It consists of two steps:
1. **Building the FP-Tree**
2. **Mining Frequent Itemsets from the FP-Tree**

## Database Integration
Integration with MongoDB allows for efficient storage and retrieval of frequent itemsets. MongoDB is a NoSQL database that provides high performance, high availability, and easy scalability. We store the generated frequent itemsets in a MongoDB collection.

**Modify each consumer to connect to one of the databases and store the results.**

## Bonus: Enhancing Project Execution with a Bash Script

Set up a bash script that runs the producer and consumers and initializes all Kafka components, like Kafka Connect, Zookeeper, etc.

### 8. Conclusion
This README file provides an overview of the frequent itemset mining project. It includes implementations of the Apriori, PCY, and FP-Growth algorithms, as well as integration with MongoDB. Additionally, it covers preprocessing of the Amazon_meta.json file using Apache Kafka Producer and Consumer. This project aims to efficiently mine frequent itemsets from large datasets for various applications.
