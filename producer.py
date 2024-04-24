from kafka import KafkaProducer
import json

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=json_serializer)

with open("dummy_data.json", 'r') as file:
    for line in file:
        producer.send("preprocessed_data", value=line)
        print(line)
        producer.flush()
