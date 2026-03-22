# Real-time fraud detection pipeline 
to detect fraud transaction
How to Run the Project (Step-by-Step)
1. Start the Kafka Infrastructure
Open your terminal in the root folder (C:\fraud_project) and start the Docker containers:

Check: Open Docker Desktop. Ensure both zookeeper-1 and kafka-1 are Solid Green.

2. Create the "Transactions" Topic
Run this command to tell Kafka where to send the data.

(If it says "already exists," you are good to go!)

3. Start the Live Monitoring (Left Terminal)
We start the Detector first so it's ready to catch fraud the moment it starts.

Wait for: ✅ CONNECTED! Monitoring for Fraud...

4. Start the Data Stream (Right Terminal)
Now, start the Producer to begin sending transactions from the CSV file.

🕵️ What You Will See (The Demo)
On the Right: You will see Sent: Transaction 1, Sent: Transaction 2...

On the Left: You will see the instant analysis: ✅ Safe: $45.00 or 🚨 FRAUD ALERT: $2400.00.
