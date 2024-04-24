from kafka import KafkaConsumer
import json
import sqlite3
from fp_growth import find_frequent_itemsets

# Define the Kafka consumer
consumer = KafkaConsumer('dummy_data.json',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: json.loads(x.decode('utf-8')))

# Parameters
window_size = 100  # Window size for the streaming process
min_support = 0.005

# Initialize variables
transactions = []

# Define function to update FP-Growth tree with new transactions
def update_fp_growth_tree(fp_growth_tree, new_transactions):
    for transaction in new_transactions:
        fp_growth_tree.add(transaction)

# Connect to SQLite database
conn = sqlite3.connect('frequent_itemsets.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS frequent_itemsets
             (itemset TEXT PRIMARY KEY NOT NULL, support REAL)''')

# Function to insert frequent itemsets into the database
def insert_frequent_itemset(itemset, support):
    c.execute("INSERT OR IGNORE INTO frequent_itemsets (itemset, support) VALUES (?, ?)", (str(itemset), support))
    conn.commit()

# Retrieve and process the data
fp_growth_tree = None
for message in consumer:
    record = message.value
    transactions.append(record['products'])
    
    if len(transactions) >= window_size:
        if fp_growth_tree is None:
            fp_growth_tree = find_frequent_itemsets(transactions, min_support=min_support, include_support=True)
        else:
            update_fp_growth_tree(fp_growth_tree, transactions)

        # Print the frequent itemsets
        print("Frequent Itemsets:")
        for itemset, support in fp_growth_tree:
            insert_frequent_itemset(itemset, support)
            print(f"Itemset: {itemset}, Support: {support}")

        # Clear transactions for the next window
        transactions = []

# Close the connection
conn.close()
