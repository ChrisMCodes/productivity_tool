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
# My goals for it are:
#
# 1. Learn enough tkinter to create a GUI
# 2. Create a data entry field that allows user to enter tasks and times
# 3. Create a start/stop button that starts and stops the countdown timer 
# 4. Measure and reward successes...maybe with inspirational cat photos?

import time
import playsound
import tkinter as tk

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
    root.after(30, destroy)
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
            label.config(text = "0:00 Time is up!")
            root.update()
            playsound.playsound("alarm.mp3")
    pass

def get_countdown_time():
    '''gets time on task from user'''
    print("Please enter the number of minutes that you would like to spend on this task: ")
    mins = input() 

    works = False

    # ensuring valid numerical floating-point value:
    while not works:
        try:
            mins = float(mins)
            works = True
        except:
            print("Please enter numerical values only.")
    return mins 

# Testing the timer logic
countdown_pop_up(get_countdown_time())

# Next steps:
#
# 1. Create a task object class that defines task objects and assigns object names and times as attributes
# 1a. The functions above may be the getters/setters for the time attribute
# 2. Ask user to enter names of tasks and times. 
# 3. Save objects to a list and call on them one at a time.
