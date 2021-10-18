from kafka import KafkaConsumer
from kafka import KafkaAdminClient
from kafka.structs import TopicPartition
consumer = KafkaConsumer('demo')

for msg in consumer:
    print(msg.value)