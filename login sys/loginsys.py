em=input("Enter the E-mail: ")
pwd=input("Enter the password: ")
re_pwd=input("Enter the password: ")
if (pwd==re_pwd):
    with open('loginsys.txt','w') as wf:
        wf.write(em)
        wf.write(" ")
        wf.write(pwd)
else:
    with open('loginsys.txt','w') as wf:
        wf.write("Error :(")
