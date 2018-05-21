from pymongo import MongoClient, errors

client = MongoClient("localhost", 27017)
db = client.test
doc = ({'time':'1','longitude':'2','latitude':'3'})
db.location.insert(doc)