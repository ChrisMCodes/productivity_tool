#!/usr/bin/env python3

#
# Updated: 2020-08-08
#
# Most recent changes: 
#
# Added GUI for countdown timer
#
# About this program:
#
# These are early development notes before I figure out exactly how to code this.
#
# Ultimately this program is an idea in progress.
# It should be a variation on the typical to-do app
# That tracks both tasks/progress on tasks and uses a countdown timer.
#
# My remaining goals for it are:
#
# 1. Create a data entry field that allows user to enter tasks and times 
# 2. Measure and reward successes...maybe with inspirational cat photos?
# 3. I should probably object-orient this for testing. Does VSC automate
#    getters and setters?
#

import sys
import time
import playsound
import tkinter as tk

# Class to store tasks
class Task():
    def __init__(self, taskname, time):
        self.taskname = taskname
        self.time = time

    def __str__(self):
        return "Task: {}; Time: {} minutes".format(self.taskname, self.time)


def add_task(tasklist):
    print("Please enter the name of your task: ")
    task_name = input()
    task_time = get_countdown_time(task_name)
    new_task = Task(task_name, task_time) 
    tasklist += [new_task]
    return tasklist
    

def countdown_pop_up(mins):
    '''creates gui for countdown'''
    root = tk.Tk()
    root.title = ("Countdown")
    label = tk.Label(root, 
                     fg = "green", 
                     font = "Arial 32 bold")
    label.pack()
    button = tk.Button(root, 
                       text = "Stop", 
                       width = 25, 
                       command = root.destroy)
    button.pack()
    countdown(root, label, mins)
    root.mainloop()
    pass

def countdown(root, label, mins):
    '''countdown for pop-up'''
    i = mins * 60
    while i >= 0:
        minutes = i / 60
        seconds = round(i % 60, 0)
        counter = "%d:%02d" % (minutes, seconds)
        label.config(text = counter)
        root.update()
        time.sleep(1)
        i -= 1
        if i == 0:
            label.config(text = "0:00 \nTime is up!")
            root.update()
            playsound.playsound("alarm.mp3")
    pass

def get_countdown_time(task):
    '''gets time on task from user'''
    print("Please enter the number of minutes that you would like to spend on {}: ".format(task))
    mins = input() 

    works = False

    # ensuring valid numerical floating-point value:
    while not works:
        try:
            mins = float(mins)
            if mins > 0:
                works = True
            else:
                print("Please restart the program. " +
                      "Ensure that you enter a value greater than 0")
                works = False
                break
        except:
            print("Please restart the program. " +
                  "Enter numerical values only.")
            sys.exit(1)
            break
    return mins 


#
#
# Here's the start of our main method
#
#

cont_task = True
affirmatives = ['yes', 'yeah', 'y', 'yes, please', 'yes please', 'ok', 'sure',
                'affirmative', 'yup', 'duh', 'of course', 'i guess', 'true',
                'for sure', 'fo sho', 'guess so', 'yeet', 'word', 'k', 'aight',
                'alright', 'indeed', 'mmhmm', 'mm-hmm', 'yep', 'yeppers']

tasklist = []

# Loops for as many tasks as the user wants to enter

while cont_task:
    add_task(tasklist)
    cont = input("Would you like to add another task (y/n)? ")
    if cont.lower() not in affirmatives:
        print("Ok, last task has been entered.")
        cont_task = False

# Loops through the tasklist and times each one 

for task in tasklist:
    print("Now working on {}.".format(task.taskname))
    countdown_pop_up(task.time)

