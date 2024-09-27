import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        result = num1 + num2
        messagebox.showinfo("result",f"the sum is:{result}")
    except ValueError:
        messagebox.showerror("input error","please enter valid integers")
root = tk.Tk()
root.title("addition")

#create and pack widgets
tk.Label(root, text="ENTER FIRST NUMBER").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack(pady=5)

tk.Label(root,text="enter second number").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack(pady=5)

tk.Button(root, text="add", command=add_numbers).pack(pady=10)
tk.Button(text="exit",command= exit).pack()

root.mainloop()    