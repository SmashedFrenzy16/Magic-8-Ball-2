import sys
import random
import time
from tkinter import *

root = Tk()

keep_going = True

while keep_going:

    def Process():

        processing = Label(root, text="Processing question...").grid(
            row=1, column=0)
        time.sleep(2)

        if question == "":
            sys.exit()

        elif answer == 1:
            Label(root, text="Your answer is yes").grid(row=1, column=0)

        elif answer == 2:
            Label(root, text="Unfortunately no").grid(row=1, column=0)

        elif answer == 3:
            Label(root, text="Maybe").grid(row=1, column=0)

        elif answer == 4:
            Label(root, text="It has a potential to").grid(row=1, column=0)

        elif answer == 5:
            Label(root, text="Sorry, try again").grid(row=1, column=0)

        elif answer == 6:
            Label(root, text="A slim chance that that would happen").grid(row=1, column=0)

        elif answer == 7:
            Label(root, text="You can hope for it").grid(row=1, column=0)

        elif answer == 8:
            Label(root, text="Well... I am not really sure of the answer").grid(row=1, column=0)

    question = Entry(root, width=100, borderwidth=5).grid(row=0, column=0)

    button1 = Button(root, text="Enter", command=Process)

    answer = random.randint(1, 8)
