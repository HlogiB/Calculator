from tkinter import *
<<<<<<< HEAD

#Hello thereew we are the master 

=======
#Aowa hlogi rocks bathong
>>>>>>> hlogi
root=Tk()

e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=20)
#This is hlogi here
def clear():

    e.delete(0,END)

def onClick(number):

    cat=e.get()
    e.delete(0, END)
    e.insert(0,str(cat)+str(number))

def add():
    math("+")

def multi():
    math("*")

def divide():
    math("/")

def minus():
    math("-")

def math(char):
    num = e.get()
    e.delete(0, END)
    global fnum
    global sym
    sym = char
    fnum = float(num)

def equal(number):
    if sym=="+":
        total = int(number) + int(e.get())
    elif sym == "*":
        total = int(number) * int(e.get())
    elif sym=="-":
        total = int(number) - int(e.get())
    elif sym=="/":
        total =float(number) / float(e.get())
    else:
        total="INVALID OPERATION!!!"

    e.delete(0,END)
    e.insert(0,total)



button1=Button(root, text="1",padx=40,pady=20,command=lambda:onClick(1))
button2=Button(root,text="2",padx=40,pady=20,command=lambda:onClick(2))
button3=Button(root,text="3",padx=40,pady=20,command=lambda:onClick(3))
button4=Button(root,text="4",padx=40,pady=20,command=lambda:onClick(4))
button5=Button(root,text="5",padx=40,pady=20,command=lambda:onClick(5))
button6=Button(root,text="6",padx=40,pady=20,command=lambda:onClick(6))
button7=Button(root,text="7",padx=40,pady=20,command=lambda:onClick(7))
button8=Button(root,text="8",padx=40,pady=20,command=lambda:onClick(8))
button9=Button(root,text="9",padx=40,pady=20,command=lambda:onClick(9))
button10=Button(root,text="0",padx=40,pady=20,command=lambda:onClick(0))
buttonadd=Button(root,text="+",padx=39,pady=20,command=add)
buttonequals=Button(root,text="=",padx=40,pady=20,command=lambda: equal(fnum))
buttonminus=Button(root,text="-",padx=40,pady=20,command=minus)
buttonmulti=Button(root,text="*",padx=40,pady=20,command=multi)
buttondivide=Button(root,text="/",padx=40,pady=20,command=divide)
buttonclear=Button(root,text="C",padx=40,pady=20,command=clear)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
buttonmulti.grid(row=1,column=3)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
buttonadd.grid(row=2,column=3)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
buttondivide.grid(row=3,column=3)

button10.grid(row=4,column=0)
buttonclear.grid(row=4,column=1)
buttonequals.grid(row=4,column=2)
buttonminus.grid(row=4,column=3)



root.mainloop()