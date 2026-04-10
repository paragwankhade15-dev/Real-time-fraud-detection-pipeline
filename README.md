# Real-time fraud detection pipeline 
Follow these steps to get the Real-time Fraud Detection Pipeline running on your local machine.

1. Prerequisites
Ensure you have the following installed:

Python 3.8+

Docker Desktop (Required for Kafka and Zookeeper)

Git

2. Clone the Repository
Open your terminal and run:

Bash
git clone https://github.com/paragwankhade15-dev/Real-time-fraud-detection-pipeline.git
cd Real-time-fraud-detection-pipeline
3. Set Up Virtual Environment (Recommended)
Bash
# Create environment
python -m venv venv

# Activate environment (Windows)
.\venv\Scripts\activate

# Activate environment (Mac/Linux)
source venv/bin/activate
4. Install Dependencies
Bash
pip install -r requirements.txt
(Note: If you don't have a requirements file yet, run pip install pandas kafka-python)

5. Start Infrastructure (Docker)
This project uses Docker to run the Kafka broker and Zookeeper.

Bash
docker-compose up -d
Wait about 30 seconds for the containers to fully initialize before moving to the next step.

6. Add the Dataset
Download the creditcard.csv dataset.

Place the file inside the data/ folder.

Ensure the filename matches the one in producer.py (e.g., creditcard copy.csv).

🚀 How to Run the Project
To see the real-time detection in action, you need to open two separate terminal windows.

Step 1: Start the Detector (Consumer)
In the first terminal, run:

Bash
python src/detector.py
You should see a message: CONNECTED! Monitoring for Fraud...

Step 2: Start the Producer
In the second terminal, run:

Bash
python src/producer.py
The producer will begin streaming transactions from the CSV to Kafka.

💡 Workshop Learning Outcomes
How to orchestrate microservices using Docker Compose.

Implementing the Producer-Consumer pattern with Apache Kafka.

Real-time data processing and threshold-based Fraud Detection logic.
