from tkinter import *

root = Tk()
root.title("loginsys")


Label_em=Label(root,text="Enter your email id: ")
Label_em.grid(row=0,column=0)

e1=Entry(root,borderwidth=5)
e1.grid(row=0,column=1)


Label2_pass=Label(root, text="Enter password: ")
Label2_pass.grid(row=1,column=0)

e2=Entry(root,borderwidth=5)
e2.grid(row=1,column=1)

Label3_pass=Label(root, text="Enter password again: ")
Label3_pass.grid(row=2,column=0)

e3=Entry(root,borderwidth=5)
e3.grid(row=2,column=1)


def click():
    em=e1.get()
    pwd1=str(e2.get())
    pwd2=str(e3.get())
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    if (pwd1==pwd2):
        with open('loginsys.txt','w') as wf:
            wf.write(em + '\n')
            wf.write(pwd1)
    else:
        Label4= Label(root,text="Error :(")
        Label4.grid()


button=Button(root,text="Done",command=click)
button.grid(row=3,column=0,columnspan=2)

root.mainloop()
