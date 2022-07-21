from kafka import KafkaConsumer
import json

if __name__=="__main__" :
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers = "localhost:9092",
        auto_offset_reset = "earliest",
        group_id = "consumer-group-a"
    )
    print("starting consumer")

    for message in consumer :
        print("registered user = {}".format(json.loads(message.value)))