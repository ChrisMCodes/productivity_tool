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
import sys
import time
import playsound

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

def countdown_pop_up(mins, taskname):
    '''creates gui for countdown'''
    root = Tk()
    root.title = ("Countdown")
    label = Label(root, 
                     fg = "green", 
                     font = "Arial 32 bold")
    label.pack()
    button = Button(root, 
                       text = "Stop", 
                       width = 25, 
                       command = root.destroy)
    button.pack()
    countdown(root, label, mins, taskname)
    root.destroy()
    root.mainloop()
    pass

def countdown(root, label, mins, taskname):
    '''countdown for pop-up'''
    i = mins * 60
    while i >= 0:
        minutes = i / 60
        seconds = round(i % 60, 0)
        counter = "%d:%02d" % (minutes, seconds)
        label.config(text = counter + "\n" + taskname)
        root.update()
        time.sleep(1)
        i -= 1
        if i == 0:
            label.config(text = "0:00 \nTime is up!")
            root.update()
            playsound.playsound("alarm.mp3")

    
# Pop up to get user info
task_button = Button(root, text="Enter your task", command=a_click)
task_button.pack()

exit_button = Button(root, text="Click here when finished", command=root.destroy)
exit_button.pack()

root.mainloop()


#Counter!
for task in tasklist:
    try:
        t = task.get_time()
        t = float(t)
        n = task.get_name()
        countdown_pop_up(t, n)
    except:
        print("Please enter valid numerical values for your times on task.")
        print("Program exiting")
        sys.exit(1)