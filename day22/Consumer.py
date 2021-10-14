from kafka import KafkaConsumer
consumer = KafkaConsumer('items')
for msg in consumer:
    print(msg)


