#import statement
from pymongo import MongoClient

#create database connection
connection = MongoClient("mongodb+srv://rhodzeey:12345@cluster0.tpb0e.mongodb.net/farm?retryWrites=true&w=majority")