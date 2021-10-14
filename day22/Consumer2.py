from kafka import KafkaConsumer
from json import loads
consumer = KafkaConsumer('check',bootstrap_servers=['localhost:9092'],auto_offset_reset='earliest',enable_auto_commit=True,group_id='my-group',value_deserializer=lambda x: loads(x.decode('ascii')))
print("Starting.....")
for message in consumer:
    print(message.value)


