from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('items',b'hii')
producer.flush()