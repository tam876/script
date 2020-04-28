import csv
from time import time
from decimal import Decimal
from faker import Faker
import datetime
from random import randint

RECORD_COUNT = 500000
fake = Faker('en_US')
count = 0

def add_quotes(word):
	return "\"" + word + "\""

def create_csv_file():
    with open('./files/prof.csv', 'w', newline='') as csvfile:
        fieldnames = ['uID','first_name', 'last_name', 'email', 'dob']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

 
        for i in range(RECORD_COUNT):
           
            writer.writerow(
                {
                    'uID': count,
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name(),
                    'email': fake.email(),
                    'dob': generateDate()
                    
                }
            )
def generateDate():
    date = datetime.date(randint(2000,2018), randint(1,12),randint(1,28))
    return date



if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file time: {}'.format(elapsed))

