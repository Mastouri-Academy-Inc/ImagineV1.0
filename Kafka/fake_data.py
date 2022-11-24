from faker import Faker
import random
from datetime import datetime

fake = Faker()

def get_registered_user() :

    full_name = fake.name()
    return {
        
        "c_email" : full_name.replace(" ", "-") + "@gmail.com",
        "firstname" : full_name.split()[0],
        "lastname" : full_name.split()[1],
        "phone" : "2126" + str(random.randint(10000000, 99999999)),
        "date_insc" : datetime.today().replace(microsecond=0),
        "waletId" : str(random.randint(10000000, 99999999))
    }

if __name__ == "__main__" :
    print(get_registered_user())