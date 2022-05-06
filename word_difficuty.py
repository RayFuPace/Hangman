import random
from crud_server2 import myCollection
document = myCollection.find_one({})

def word_adjust():
    cursor = myCollection.find()
    for each_document in cursor:
        print (each_document ["word"])

    word_adjust = input(str("please select a word to adjust:"))
    difficulty_adjust = input(str("what is the new difficulty:"))

    myCollection.update_one(
        {"word": word_adjust},
        {"$set": {"difficulty": difficulty_adjust } }
    )
    