import pandas as pd
from kafka import KafkaProducer
import json
import time

print("--- 🔄 Connecting to Kafka ---")

try:
    # We are using the direct IP address to bypass Windows network issues
    producer = KafkaProducer(
        bootstrap_servers=['127.0.0.1:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8'),
        api_version=(0, 10, 1),
        max_block_ms=5000  # If it can't connect in 5 seconds, it will tell us
    )
    print("✅ PRODUCER CONNECTED!")
except Exception as e:
    print(f"❌ Connection Error: {e}")
    exit()

# Try to load your data
try:
    df = pd.read_csv('creditcard.csv')
    print(f"📊 CSV Loaded: {len(df)} rows found.")
except:
    df = pd.read_csv('creditcard copy.csv')
    print(f"📊 CSV (Copy) Loaded: {len(df)} rows found.")

print("🚀 Starting stream now...")

for index, row in df.iterrows():
    try:
        producer.send('transactions', value=row.to_dict())
        print(f"Sent: Transaction {index}")
        time.sleep(1)
    except Exception as e:
        print(f"❌ Error sending: {e}")
        break
