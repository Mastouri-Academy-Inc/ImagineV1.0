from data import get_registered_user
from kafka import KafkaProducer
import json
from data import get_registered_user
import time
from ksql import KSQLAPI

client = KSQLAPI('http://localhost:8088') # Setting up the client API


def json_serializer(data) :
    return json.dumps(data).encode("utf-8")

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=json_serializer)

if __name__ == "__main__" :
    while True :
        registered_user = [get_registered_user()]
        print(registered_user)
        results = client.inserts_stream("registered_user_stream", registered_user)
        print(results)
        #producer.send("registered_user", data)
        time.sleep(3)