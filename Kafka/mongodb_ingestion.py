import pymongo
import urllib
import datetime

username = urllib.parse.quote_plus('admin')
password = urllib.parse.quote_plus('NAq8::Zp3GXzR-V')
client = pymongo.MongoClient("mongodb+srv://{}:{}@imagine.3ulxs7w.mongodb.net/ImagineDB?retryWrites=true&w=majority".format(username, password))

mydb = client["ImagineDB"]
mycol = mydb["Citizen"]

d = datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")

mydict = {'c_email': 'Kristin-Austin@gmail.com', 'firstname': 'Kristin', 'lastname': 'Austin', 'phone': '212667859499', 'date_insc': d, 'c_password': '69207706'}

x = mycol.insert_one(mydict)