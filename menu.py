from hangman2 import main
from word_creation import word_creation
from word_difficuty import word_adjust
from word_delete import word_delete


command = 0

while command == 0:
       
       print ("""Hello welcome to the termonal. What would ypu like to do?
       1. Play Hang-Man (Read)
       2. Add a word to word bank  (Create)
       3. Update and entry (Update)
       4. Delete an entry
       5. Exit
       """)
       
       command = input("What is your command:")
       if command == "1":
              main()
              command = 0
       elif command == "2":
              word_creation()
              command = 0
       elif command == "3":
              word_adjust()
              command = 0
       elif command == "4":
              word_delete()
              command = 0
       elif command == "5":
              exit

       
