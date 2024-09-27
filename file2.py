#Tkinter 
from tkinter import *
from tkinter import messagebox as msgbox

root = Tk()
root.title('My First Interface Developed')

userVariable = StringVar()
passVariable = StringVar()

uLabel = Label(root, text="Username!")
uEntry = Entry(root, textvariable=userVariable)
pLabel = Label(root, text="Password!")
pEntry = Entry(root, textvariable=passVariable, show="*")
text = Text(root, width=30, height=3)
text.insert(1.0, "I have been added \nI am on teh second line")
#text.insert(2.0, "This is line 2"), 
#getting from text widget
#print(text.get(1.0, 1.4))
errLabel = Label(root, text='passin correct credentials')

def auth():
    username = uEntry.get()
    password = pEntry.get()
    if username == "1234" and password == "1234":
        print(f'Username = {username} and Password {password}')
        uEntry.delete(0, END)
        pEntry.delete(0, END)
        uEntry.insert(0, 'I have been inserted!')
        msgbox.showinfo(title='success', message='authentication successfull!')
    else:
        print('please try again!')
        errLabel.config(text="invalid uname and password combination")
        msgbox.showerror(title='Error', message="invalid uname and password combination")

btn = Button(root, text='authenticate', command=auth)

uLabel.pack()
uEntry.pack()
pLabel.pack()
pEntry.pack()
btn.pack()
errLabel.pack()
text.pack()
root.mainloop()