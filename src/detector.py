from kafka import KafkaConsumer
import json
import time

print("--- Connecting to Kafka ---")

# Try to connect up to 5 times
for i in range(5):
    try:
        consumer = KafkaConsumer(
            'transactions',
            bootstrap_servers=['localhost:9092'],
            auto_offset_reset='earliest',
            value_deserializer=lambda x: json.loads(x.decode('utf-8')),
            # This helps wait for the broker to be ready
            api_version=(0, 10, 1) 
        )
        print("✅ CONNECTED! Monitoring for Fraud...")
        break
    except Exception as e:
        print(f"❌ Attempt {i+1} failed... retrying in 5 seconds")
        time.sleep(5)
else:
    print("❌ Could not connect to Kafka. Check if Docker is running!")
    exit()

for message in consumer:
    tx = message.value
    if tx['Amount'] > 500:
        print(f"🚨 FRAUD ALERT: ${tx['Amount']}")
    else:
        print(f"✅ Safe: ${tx['Amount']}")
