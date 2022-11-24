import os
import pymongo
from bson.json_util import dumps
import urllib
import time
from ksql import KSQLAPI
from kafka import KafkaProducer
import json

def json_serializer(data) :
    return json.dumps(data).encode("utf-8")

#client_ksql = KSQLAPI('http://localhost:8088') # Setting up the client API
producer = KafkaProducer(bootstrap_servers=['192.168.93.128:9092'], value_serializer=json_serializer)

username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('NAq8::Zp3GXzR-V')
client = pymongo.MongoClient("mongodb+srv://{}:{}@imagine.3ulxs7w.mongodb.net/ImagineDB?retryWrites=true&w=majority".format(username, password))


pipeline = [
            {"$match": {"operationType": {"$in": ["insert", "delete", "replace", "update"]}}},
            {"$match": {"ns.db": "ImagineDB"}},
            {"$match": {"ns.coll": ["Testing", "Citizen", "Admin"]}}
]

change_stream = client.watch(full_document="updateLookup",
            pipeline=pipeline)

# def json_serializer(data) :
#     return json.dumps(data).encode("utf-8")

for change in change_stream:

    print(dumps(change))
    print('') # for readability only

    changed_data = [dumps(change)]
    #results = client_ksql.inserts_stream("insert_stream", changed_data)
    #print(results)
    producer.send("ImagineDB.Testing", changed_data)
    time.sleep(1)