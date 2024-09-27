#Import the required libraries
from tkinter import *

#Create an instance of tkinter frame
win= Tk()

#Set the geometry of frame
win.geometry("600x350")

def close_win():
   win.destroy()
def print():
   user = username.get()
   password = password.get()
   print("username:",user)
   print("password:",password)
#Create a text label
Label(win,text="Enter the Username", font=('Helvetica',20)).pack(pady=20)
#Create Entry Widget for password
username= Entry(win,width=20)
username.pack()
#Create a text label
Label(win,text="Enter the Password", font=('Helvetica',20)).pack(pady=20)

#Create Entry Widget for password
password= Entry(win,show="*",width=20)
password.pack()

#Create a button to close the window
Button(win, text="Quit", font=('Helvetica bold',
10),command=close_win).pack(pady=20)

Button(win, text="show", font=('Helvetica bold',
10),command=print).pack(padx=20)

win.mainloop()
