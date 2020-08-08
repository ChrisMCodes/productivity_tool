#!/usr/bin/env python3

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

def countdown(mins):
    i = mins * 60
    while i > 0:
        minutes = i / 60
        seconds = i % 60
        print("%d:%02d" % (minutes, seconds))
        time.sleep(1)
        i -= 1
    print("Time's up!")
    pass

def get_countdown_time():
    print("Please enter the number of minutes that you would like to spend on this task. Enter whole numbers only: ")
    count = input() 
    while not count.isdigit():
        print("Please enter integer values only.")
        count = input()
    count = int(count)
    return count 

# Testing the timer logic
countdown(get_countdown_time())

# Next steps:
#
# 1. Create a task object class that defines task objects and assigns object names and times as attributes
# 1a. The functions above may be the getters/setters for the time attribute
# 2. Ask user to enter names of tasks and times. 
# 3. Save objects to a list and call on them one at a time.