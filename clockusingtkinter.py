from tkinter import *
import tkinter as tk
import time

root=Tk()

#initiating tkinter object and setting background colour
root.configure(bg='navajo white')

# create a label object to display time
label=Label(root,font='comiscsans 50',bg='navajo white')
label.pack()

#create a function to display the time
def time():
    current_time=time.strftime("%H:%M:%S:%p")
    label.configure(text=Current_time)
    label.after(200,time)# after() is used to update the display on the screen

# call the function to display time 
time()

#call to mainloop
root.mainloop()
