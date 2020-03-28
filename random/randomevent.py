import turtle
import random

turtle1=turtle.Turtle()
i=0
sum=0

while (sum<=333):
    num=random.random()*4
    turtle1.forward(num)
    i=i+1
    sum=sum + num

int_to_string=str(i)

with open('steps.txt','w') as wf:
    wf.write("The number of steps it took was ")
    wf.write(int_to_string)
    
    







