from confluent_kafka import Consumer, KafkaError

# Configure the Kafka consumer
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Create three consumer instances
consumer1 = Consumer(conf)
consumer2 = Consumer(conf)
consumer3 = Consumer(conf)

# Subscribe consumers to the topic
consumer1.subscribe(['preprocessed_data'])
consumer2.subscribe(['preprocessed_data'])
consumer3.subscribe(['dummy_data.json'])

# Poll for messages
try:
    while True:
        # Poll for messages for each consumer
        msg1 = consumer1.poll(1.0)
        msg2 = consumer2.poll(1.0)
        msg3 = consumer3.poll(1.0)

        if msg1 is None and msg2 is None and msg3 is None:
            continue

        # Handle messages received by consumer1
        if msg1 is not None:
            if msg1.error():
                if msg1.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg1.error())
            else:
                print('Consumer 1: {}'.format(msg1.value().decode('utf-8')))

        # Handle messages received by consumer2
        if msg2 is not None:
            if msg2.error():
                if msg2.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg2.error())
            else:
                print('Consumer 2: {}'.format(msg2.value().decode('utf-8')))

        # Handle messages received by consumer3
        if msg3 is not None:
            if msg3.error():
                if msg3.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg3.error())
            else:
                print('Consumer 3: {}'.format(msg3.value().decode('utf-8')))

except KeyboardInterrupt:
    consumer1.close()
    consumer2.close()
    consumer3.close()
