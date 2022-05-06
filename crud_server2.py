import random
import pymongo
from pymongo import MongoClient
client=pymongo.MongoClient('localhost', 27017)
mydb = client["Hangman_Database"]
myCollection = mydb["Hangman_Collection"]
