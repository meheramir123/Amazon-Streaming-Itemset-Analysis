from kafka import KafkaConsumer
import json
from apyori import apriori

# Define the Kafka consumer
consumer = KafkaConsumer('dummy_data.json',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Parameters
window_size = 100  # Window size for the streaming process
min_support = 0.005
min_confidence = 0.2
min_lift = 3
min_length = 2

# Initialize variables
transactions = []

# Retrieve and process the data
for message in consumer:
    record = message.value
    transactions.append(record['products'])
    
    if len(transactions) >= window_size:
        association_rules = apriori(transactions, min_support=min_support, min_confidence=min_confidence, min_lift=min_lift, min_length=min_length)
        association_results = list(association_rules)

        # Print the association rules
        for item in association_results:
            pair = item[0]
            items = [x for x in pair]
            print("Rule: " + str(items[0]) + " -> " + str(items[1]))
            print("Support: " + str(item[1]))
            print("Confidence: " + str(item[2][0][2]))
            print("Lift: " + str(item[2][0][3]))
            print("=====================================")

        # Reset transactions
        transactions = []
