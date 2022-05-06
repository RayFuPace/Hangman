from crud_server2 import myCollection

#Get Inputs
def word_creation ():
    x = input(str("Give me a word:"))
    y = input(str("""
              1. Easy 2. Medium 3. Hard 
              Whats the difficulty ?"""))

    #Create a word
    myCollection.insert_one(
        {
    "word": x,
    "difficulty": y
        }
    )
