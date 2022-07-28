from faker import Faker
import random
import datetime

fake = Faker()

def get_registered_user() :

    full_name = fake.name()
    current_date = datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
    return {
        
        "c_email" : full_name.replace(" ", "-") + "@gmail.com",
        "firstname" : full_name.split()[0],
        "lastname" : full_name.split()[1],
        "phone" : "2126" + str(random.randint(10000000, 99999999)),
        "date_insc" : str(current_date),
        "c_password" : str(random.randint(10000000, 99999999))
    }

if __name__ == "__main__" :
    print(get_registered_user())