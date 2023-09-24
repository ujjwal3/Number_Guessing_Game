from tkinter import *
from tkinter.messagebox import *
import random


def btn1():
    global num
    num = random.randint(minvar.get(), maxvar.get())


def btn2():
    global num
    if num == yourguessvar.get():
        showinfo("Result",f"Congratulations! Your Guess {yourguessvar.get()} is Currect")
    elif num < yourguessvar.get():
        showinfo("Result","Your Guess Is Too High")
    elif num > yourguessvar.get():
        showinfo("Result","Your Guess Is Too Low")



root = Tk()
root.geometry("300x300")
root.title("Number Guessing Game")

min = Label(root, text="Enter Minimum Number")
min.pack()
minvar = IntVar()
minentry = Entry(root, textvariable=minvar)
minentry.pack()

max = Label(root, text="Enter Maximum Number")
max.pack()
maxvar = IntVar()
maxentry = Entry(root, textvariable=maxvar)
maxentry.pack()

submitbtn1 = Button(root, text="Submit To Get Random Number", command=btn1)
submitbtn1.pack()


yourguess = Label(root, text="Enter Your Guess")
yourguess.pack()
yourguessvar = IntVar()
myentry = Entry(root, textvariable=yourguessvar)
myentry.pack()

submitbtn2 = Button(root, text="Submit Your Guess", command=btn2)
submitbtn2.pack()

root.mainloop()
