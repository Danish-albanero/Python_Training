import requests
from kafka import KafkaProducer
import json
from json import dumps


URL = "http://127.0.0.1:8000/studentapi/"

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer = lambda x: dumps(x).encode('ascii'))

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id': id}
    
    json_data = json.dumps(data)
    

    r = requests.get(url=URL, data=json_data)
    #data = r.json()
    data = r.json()
    #print(data)
    return data
    
    
    
    #producer.send('check', value = data )
    
    



a= get_data(2)
print(a)

producer.send('check', value = a)
producer.flush()


