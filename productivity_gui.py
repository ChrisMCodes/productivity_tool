#!/usr/bin/env python3

# This is just an experiment to see if I can figure out how to make the gui work for Productivity_tool.py
# It's quite immature for now -- I need to figure out how to store the text in a list when the button is pressed
# so that it can be used as a tasklist later

from tkinter import *



root = Tk()

e = Entry(root, width=12) # creating input box
e.pack()

def a_click():
    choice = e.get()
    label = Label(root, text=choice + "added to your tasklist")
    label.pack()

    

button = Button(root, text="Enter your task", command=a_click)
button.pack()

root.mainloop()

