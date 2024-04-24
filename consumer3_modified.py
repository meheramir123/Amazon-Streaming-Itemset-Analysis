# MongoDB connection
client = MongoClient('localhost', 27017)
db = client['apriori_db']
collection = db['association_rules']

# Configure the Kafka consumer
conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer_group',
    'auto.offset.reset': 'earliest'
}

# Define the PCY algorithm
def pcy(data, hash_bucket_size, min_support=0.1, min_confidence=0.5):
    baskets = []
    item_counts = defaultdict(int)
    pair_counts = defaultdict(int)

    # Read the data and create baskets
    for basket in data:
        baskets.append(set(basket.split(',')))
        for item in baskets[-1]:
            item_counts[item] += 1

    n = len(baskets)
    min_support_count = int(min_support * n)

    # First pass
    for basket in baskets:
        for item in basket:
            item_counts[item] += 1
        for pair in combinations(basket, 2):
            hash_value = hash((pair[0], pair[1])) % hash_bucket_size
            pair_counts[hash_value] += 1

    # Second pass
    frequent_itemsets = []
    for item, count in item_counts.items():
        if count >= min_support_count:
            frequent_itemsets.append(item)

    # Third pass
    for pair, count in pair_counts.items():
        if count >= min_support_count:
            item1, item2 = pair
            if item1 in frequent_itemsets and item2 in frequent_itemsets:
                support_itemset = count / n
                support_item1 = item_counts[item1] / n
                confidence = support_itemset / support_item1
                if confidence >= min_confidence:
                    association_rule = {"item1": item1, "item2": item2, "support": support_itemset, "confidence": confidence}
                    print("Association Rule: {} => {} , Support: {:.2f}, Confidence: {:.2f}".format(item1, item2, support_itemset, confidence))
                    # Store association rule in MongoDB
                    collection.insert_one(association_rule)

try:
    data = []
    while True:
        # Poll for messages
        msg = consumer.poll(1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        # Handle message
        line = json.loads(msg.value().decode('utf-8'))
        basket = line["basket"]
        print("Received:", basket)
        data.append(basket)

        # Run PCY algorithm on the received data
        pcy(data, hash_bucket_size=1000, min_support=0.05, min_confidence=0.5)

except KeyboardInterrupt:
    consumer.close()
