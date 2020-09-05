
from tkinter import*
import math
def btnClick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)

def btnClear():
    global operator
    operator=""
    text_input.set("")

def btnEquals():
    global operator
    eql=str(eval(operator))
    text_input.set(eql)
    return

'''def btnPi():
    global operator
    pi=math.pi
    return pi'''

def sqroot():
    global operator
    sroot=(math.sqrt(int(operator)))
    text_input.set(sroot)

def square():
    global operator
    p=math.pow(int(operator),2)
    text_input.set(p)

def tenPower():
    global operator
    po=math.pow(10,int(operator))
    text_input.set(po)
    
cal=Tk()
cal.title("calculator")
operator=""
text_input=StringVar()
txtDisplay=Entry(cal,font=('ariel',20,'bold'),textvariable=text_input,bd=30,insertwidth=4,bg="rosy brown",justify='right').grid(columnspan=4)
btnPo=Button(cal,padx=16,bd=8,fg="black",font=('ariel',18,'bold'),text="10^",command=tenPower,bg="snow3").grid(row=5,column=0)
btn7=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 7  ",command=lambda:btnClick(7),bg="snow3").grid(row=1,column=0)
btn8=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 8  ",command=lambda:btnClick(8),bg="snow3").grid(row=1,column=1)
btn9=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 9  ",command=lambda:btnClick(9),bg="snow3").grid(row=1,column=2)
Addition=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" +",command=lambda:btnClick('+'),bg="snow3").grid(row=2,column=3)
btn4=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 4  ",command=lambda:btnClick(4),bg="snow3").grid(row=2,column=0)
btn5=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 5  ",command=lambda:btnClick(5),bg="snow3").grid(row=2,column=1)
btn6=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 6  ",command=lambda:btnClick(6),bg="snow3").grid(row=2,column=2)
Subtraction=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text="  -",command=lambda:btnClick('-'),bg="snow3").grid(row=3,column=3)
btn1=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 1  ",command=lambda:btnClick(1),bg="snow3").grid(row=3,column=0)
btn2=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 2  ",command=lambda:btnClick(2),bg="snow3").grid(row=3,column=1)
btn3=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 3  ",command=lambda:btnClick(3),bg="snow3").grid(row=3,column=2)
Multiplication=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" * ",command=lambda:btnClick('*'),bg="snow3").grid(row=4,column=3)
btn0=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" 0  ",command=lambda:btnClick(0),bg="snow3").grid(row=4,column=0)
btnClear=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',17,'bold'),text="AC",command=btnClear,bg="snow3").grid(row=1,column=3)
btnEquals=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text=" =",command=btnEquals,bg="snow3").grid(row=5,column=3)
Division=Button(cal,padx=16,bd=8,fg="Black",font=('ariel',20,'bold'),text="  /  ",command=lambda:btnClick('/'),bg="snow3").grid(row=4,column=2)

SquareRoot=Button(cal,padx=16,bd=8,fg="black",font=('ariel',20,'bold'),text=" √ ",command=sqroot,bg="snow3").grid(row=4,column=1)
Power=Button(cal,padx=16,bd=8,fg="black",font=('ariel',18,'bold'),text=" ^2",command=square,bg="snow3").grid(row=5,column=1)
Dot=Button(cal,padx=16,bd=8,fg="black",font=('ariel',20,'bold'),text="  .  ",command=lambda:btnClick('.'),bg="snow3").grid(row=5,column=2)
cal.mainloop()
