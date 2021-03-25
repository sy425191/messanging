from pymongo import MongoClient
from datetime import datetime
from termcolor import colored


cluster = MongoClient("mongodb+srv://admin:Hack#2@cluster0.bbw9b.mongodb.net/<dbname>?retryWrites=true&w=majority")

#username and password to collect from pymango website
db = cluster["username here"]["password here"]

all = db.find({})


date = datetime.now().strftime("%x")


for messages in all :
	try:
		if date != messages["date"]:
			print("Today - " + {messages['time']})
		else:
			print({messages['date']} - {messages['time']})
		print("From : " + messages['id'])
		print("message : " +  messages['message'])
		print("---------------------------------")

	except:
		pass


person = input("Name: ")
message = input("Message: ")

time = datetime.now().strftime("%X")

msg = {"id": person, "message":message, "date":date, "time":time}
db.insert_one(msg)
