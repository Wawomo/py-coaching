#Tkinter 
from tkinter import *

root = Tk()
root.title('My First Interface Developed')
#root.geometry('300x300')

userVariable = StringVar()
passVariable = StringVar()

uLabel = Label(root, text="Username!")
uEntry = Entry(root, textvariable=userVariable)
pLabel = Label(root, text="Password!")
pEntry = Entry(root, textvariable=passVariable, show="*")
bioLabel = Label(root, text="Enter your Bio Data!")
bioData = Text(root, width=30, height=5)
listLabel = Label(root, text="Registered Students!")
listOfNames = Listbox(root)
listOfNames.insert(1, 'David Hope')
listOfNames.insert(2, 'nandala mafabi')
listOfNames.insert(3, 'mathew')
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
btn1 = Checkbutton(root, text="option 1", variable=check1, onvalue=1, offvalue=0)
btn2 = Checkbutton(root, text="option 2", variable=check2, onvalue=1, offvalue=0)
btn3 = Checkbutton(root, text="option 3", variable=check3, onvalue=1, offvalue=0)

radioV = StringVar(value="1")
#dictionary for the creation 
values = {
    "Radio 1":"1",
    "Radio 2":"2",
    "Radio 3":"3"
}
for k, v in values.items():
    Radiobutton(root, text=k, value=v, variable=radioV).pack(side=BOTTOM)

btn = Button(root, text='authenticate')

uLabel.pack()
uEntry.pack()
pLabel.pack()
pEntry.pack()
bioLabel.pack()
bioData.pack()
listLabel.pack()
listOfNames.pack()
btn1.pack()
btn2.pack()
btn3.pack()
btn.pack()
root.mainloop()