from kafka import KafkaAdminClient
from kafka.admin import NewPartitions
from kafka import KafkaProducer


topic = 'demo'
bootstrap_servers = 'localhost:9092'

admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
topic_partitions = {}
topic_partitions[topic] = NewPartitions(total_count=3)
admin_client.create_partitions(topic_partitions)

producer = KafkaProducer(bootstrap_servers='localhost:9092')

producer.send('items',b'hii',partition =0)
producer.send('items',b'hii',partition = 1)

producer.send('items',b'hii',partition =0)
producer.send('items',b'hii',partition =1)
producer.send('items',b'hii',partition =2)
producer.send('items',b'hii',partition =0)
producer.send('items',b'hii',partition =2)
producer.send('items',b'hii',partition =1)
producer.send('items',b'hii',partition =1)
producer.send('items',b'hii',partition =0)
producer.send('items',b'hii',partition =1)

producer.flush()