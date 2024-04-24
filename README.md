# Amazon-Streaming-Itemset-Analysis
This project aims to analyze a sampled dataset from Amazon using streaming data processing techniques and frequent itemset mining algorithms.
This repository hosts a streaming frequent itemset mining implementation using Apache Kafka. The system comprises several components, including:

## Preprocessing

Before starting the frequent itemset mining, the data needs to be preprocessed.

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

**1. Develop a producer application that streams the preprocessed data in real-time.**

The producer application streams the preprocessed data to the Kafka topic `preprocessed_data`.

**2. Create three consumer applications that subscribe to the producer's data stream.**

Three consumers are created, where each one subscribes to the Kafka topic `preprocessed_data`.

## Frequent Itemset Mining

Once the data is available in the Kafka topic `preprocessed_data`, we can perform frequent itemset mining.

### Features:

**Apriori Consumer:**

This consumer implements the Apriori algorithm.

**PCY Consumer:**

This consumer implements the PCY algorithm.

**FP-Growth Consumer:**

This consumer implements the FP-Growth algorithm.

## Database Integration

**Modify each consumer to connect to one of the databases and store the results.**

## Bonus: Enhancing Project Execution with a Bash Script

Set up a bash script that runs the producer and consumers and initializes all Kafka components, like Kafka Connect, Zookeeper, etc.
