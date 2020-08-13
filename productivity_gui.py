#!/usr/bin/env python3

#
# Update on 2020-08-12: I made this part of the program quite functional.
# I may just adapt the other part and finish this off.
#
#
# This is just an experiment to see if I can figure out how to make the gui work for Productivity_tool.py
# It's quite immature for now -- I need to figure out how to store the text in a list when the button is pressed
# so that it can be used as a tasklist later

from tkinter import *

class Task():
    def __init__(self, name, time):
        self.name = name 
        self.time = time

    def get_name(self):
        return self.name
    
    def get_time(self):
        return self.time

    def set_name(self, name):
        self.name = name

    def set_time(self, time):
        self.time = time
    

global tasklist

tasklist = []

root = Tk()

root.title("Generating Tasklist")
l = Label(root, text = "Please enter your task in the top input field " +
                       "and the number of minutes you will spend on it in the bottom input field.")
n = Entry(root, width=12) # creating input box for name
n.pack()
t = Entry(root, width=10) # input box for time
t.pack()


def a_click():
    name = str(n.get())
    time = str(t.get())
    task = Task(name, time)
    tasklist.append(task)
    label = Label(root, text=name + " added to your tasklist")
    label.pack()




    

button = Button(root, text="Enter your task", command=a_click)
button.pack()

root.mainloop()

for task in tasklist:
    print("{} for {} mins".format(task.get_name(), task.get_time()))
