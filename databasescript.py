import csv
from time import time
from decimal import Decimal
from faker import Faker
import datetime
from random import randint
import random

RECORD_COUNT = 10
fake = Faker('en_US')
count = 0

def create_csv_user():
    with open('./files/user.csv', 'w', newline='') as csvfile:
        fieldnames = ['uID','first_name', 'last_name', 'email', 'dob','pswd']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

 
        for i in range(RECORD_COUNT):
           
            writer.writerow(
                {
                    'uID': count,
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name(),
                    'email': fake.email(),
                    'dob': generateDate(),
                    'pswd':password_generator(),
                    
                    
                }
                
            )
            
def create_csv_comments():
    with open('./files/comment.csv', 'w', newline='') as csvfile:
        fieldnames = ['uID','comment','created_at']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

 
        for i in range(RECORD_COUNT):
           
            writer.writerow(
                {
                    'uID': count,
                    'comment': fake.sentence(),
                    'created_at': generateDate()
                }
                
            )
def create_csv_content_editors():
    with open('./files/content_editors.csv', 'w', newline='') as csvfile:
        fieldnames = ['uID','editior_first_name','editior_last_name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

 
        for i in range(RECORD_COUNT):
           
            writer.writerow(
                {
                    'uID': count,
                    'editior_first_name': fake.first_name(),
                    'editior_last_name': fake.last_name()
                }
                
            )
def create_csv_group():
    with open('./files/group.csv', 'w', newline='') as csvfile:
        fieldnames = ['uID','groupName','date_created','first_name','last_name', 'date_joined']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

 
        for i in range(RECORD_COUNT):
           
            writer.writerow(
                {
                    'uID': count,
                    'groupName': fake.color_name(),
                    'date_created': generateDate(),
                    'first_name': fake.first_name(),
                    'last_name': fake.last_name(),
                    'date_joined': generateDate()
                }
                
            )

def create_csv_post():
    with open('./files/post.csv', 'w', newline='') as csvfile:
        fieldnames = ['uID','caption','post_type','post_date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

 
        for i in range(RECORD_COUNT):
           
            writer.writerow(
                {
                    'uID': count,
                    'caption': fake.word()
                    'post_type': fake.file_name(),
                    'post_date': generateDate()
                    
                }
                
            )
            
def generateDate():
    date = datetime.date(randint(2000,2018), randint(1,12),randint(1,28))
    return date

def password_generator():
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?_=+/><,.`~"
    passlen = random.randint(5,26)
    password =  "".join(random.sample(s,passlen))
    return password

if __name__ == '__main__':
    start = time()
    create_csv_comments()
    create_csv_content_editors()
    create_csv_user()
    create_csv_group()
    create_csv_post()
    elapsed = time() - start
    