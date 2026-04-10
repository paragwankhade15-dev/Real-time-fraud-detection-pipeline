https://www.kaggle.com/datasets/arockiaselciaa/creditcardcsv?resource=download
## 📝 Implementation Steps
1. **Infrastructure:** Start Kafka/Zookeeper via Docker Compose.
2. **Topic Creation:** Kafka automatically creates the `transactions` topic on the first message.
3. **Producer Engine:** Ingests CSV data and streams it to the broker.
4. **Consumer Logic:** Filters streams in real-time to identify high-risk transactions.
