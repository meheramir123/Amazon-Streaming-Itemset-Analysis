from kafka import KafkaProducer
import json

# Initialize KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

# Initialize SparkSession
spark = SparkSession.builder.appName("CSV_Kafka_Producer").getOrCreate()

# Load data from CSV
data = spark.read.text("Ball_by_Ball.csv")

# Convert data to RDD
rdd = spark.sparkContext.textFile("Ball_by_Ball.csv").map(lambda x: x.split(","))

# Send data to different Kafka topics based on columns
for doc in rdd.collect():
    topic = doc[0]  # Assuming the first column is the topic
    producer.send(topic, doc)

# Close the producer
producer.close()

