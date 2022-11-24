from kafka import KafkaConsumer
import json

if __name__=="__main__" :
    consumer = KafkaConsumer(
        "ImagineDB.Testing",
        bootstrap_servers = "localhost:9092",
        auto_offset_reset = "earliest",
        group_id = "consumer-group-a"
    )
    print("starting consumer")

    for message in consumer :

        try :
            print("Change event = {}".format(json.loads(message.value)))
        except:
            print("")