import random
from crud_server2 import myCollection
document = myCollection.find_one({})

def word_delete():
    cursor = myCollection.find()
    for each_document in cursor:
        print (each_document ["word"])

    delete =  input(str("Please enter the word for deletion:"))
    
    myCollection.delete_one(
        {"word": delete}
    )
