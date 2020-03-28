from tkinter import *

def click():
    label= Label(root, text="you perv :0")
    label.pack()

root = Tk()
button= Button(root, text="touch me ;)", fg="red",command=click, padx=10, pady=10)
button.pack()
root.mainloop()
