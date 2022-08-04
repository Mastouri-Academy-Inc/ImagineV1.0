import pymongo
import urllib
import datetime
from fake_data import get_registered_user
import time

username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('NAq8::Zp3GXzR-V')
client = pymongo.MongoClient("mongodb+srv://{}:{}@imagine.3ulxs7w.mongodb.net/ImagineDB?retryWrites=true&w=majority".format(username, password))

mydb = client["ImagineDB"]
mycol = mydb["Citizen"]


for i in range (10) :

    try :

        fake_data = get_registered_user()

        print("Adding new citizen ..")
        print("")

        x = mycol.insert_one(fake_data)

        print(f"Added : {fake_data}")
        print("")

        time.sleep(5)
    except :
        print("")

print("Added 10 new users !")
