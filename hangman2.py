import random
from asciiart import stages
from crud_server2 import myCollection




def get_word():
    
    my_difficulty = str(input("""
            1. Easy
            2. Medium
            3. Hard
    Please enter a difficulty: """ ))

    records = (myCollection.find({"difficulty" : my_difficulty}))
    special = random.choice(list(records))
    secret = (special ["word"])
    print (secret)
    return secret.upper()
    
def play(secret): #Hangman game
    word_completion = "_" * len(secret)
    tries = 0
    guessed = False
    guessed_letters = [ ]
    guessed_words = []
    print("Lets play Hangman")
    print(stages[tries])
    print(word_completion)
    print("\n")
    
    while not guessed and tries !=6:
        guess = input("Please enter a letter or word:").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:  
                print("You already guessed that letter pick another letter:")
            
            elif guess not in secret:
                print(guess, "not in the word")
                guessed_letters.append(guess)
                tries += 1
            
            else:
                print("Congrats" ,guess, "is in the word")
                guessed_letters.append(guess)
                secret_list = list(word_completion)
                myindex = [i for i, letters in enumerate(secret) if letters == guess]
                for index in myindex:
                    secret_list[index] = guess
                word_completion = "".join(secret_list)
                if "_" not in word_completion:
                    guessed = True
                
        elif len(guess) == len(secret) and guess.isalpha():
            if guess in guessed_words:
                print("You have already guess",guess," try another:")
                
            elif guess not in secret:
                print(guess, "is not the word" )
                guessed_words.append(guess)
                tries += 1 
                
            else:
                guessed = True
                word_completion = secret
                
                
        else:
            print("Not a valid guess")
        
        
        print(stages[tries])
        print(word_completion)
        print("\n")

    if guessed:
        print ("CONGRATS")
    else:
        print ("The word was",secret,"Maybe next time.")
    
    
def main(): 
    secret = get_word()
    play(secret)

