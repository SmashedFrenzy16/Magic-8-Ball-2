import sys
import random
import time

keep_going = True

while keep_going:

    question = input("Ask me a question: ")

    answer = random.randint(1, 8)

    print("Processing question...")
    time.sleep(2)

    if question == "":
        sys.exit()

    elif answer == 1:
        print("Your answer is yes")
    
    elif answer == 2:
        print("Unfortunately no")
    
    elif answer == 3:
        print("Maybe")

    elif answer == 4:
        print("It has a potential to")

    elif answer == 5:
        print("Sorry, try again")
        
    elif answer == 6:
        print("A slim chance that that would happen")

    elif answer == 7:
        print("You can hope for it")
    
    elif answer == 8:
        print("Well... I am not really sure of the answer")