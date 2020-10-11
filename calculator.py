from tkinter import *

root = Tk()
# root.geometry("500x500")
root.title("Simple Calculator")

e = Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

#1. Making Input Fields & Buttons
#2. Let the user select between +, -, * or /
#3. Call the desired function and perform the operation
#4. Show the output

def click(number):
    num = e.get()
    e.delete(0, END)
    e.insert(0, str(num) + str(number))

def clear():
    e.delete(0, END)

def equals():
    second_number = e.get()
    e.delete(0, END)

    if math=="Addittion":
        e.insert(0, f_num + int(second_number))

    elif math=="Subtraction":
        e.insert(0, f_num - int(second_number))
    
    elif math=="Multiplication":
        e.insert(0, f_num * int(second_number))
    
    elif math=="Division":
        e.insert(0, f_num / int(second_number))

def add():
    number1 = e.get()
    global f_num
    global math
    math="Addittion"
    f_num = int(number1)
    e.delete(0, END)

def sub():
    number1 = e.get()
    global f_num
    global math
    math="Subtraction"
    f_num = int(number1)
    e.delete(0, END)

def mul():
    number1 = e.get()
    global f_num
    global math
    math="Multiplication"
    f_num = int(number1)
    e.delete(0, END)

def div():
    number1 = e.get()
    global f_num
    global math
    math="Division"
    f_num = int(number1)
    e.delete(0, END)

#Making Buttons
button_1 = Button(root,text="1",padx=50,pady=30, command=lambda : click(1))
button_2 = Button(root,text="2",padx=50,pady=30, command=lambda : click(2))
button_3 = Button(root,text="3",padx=50,pady=30, command=lambda : click(3))
button_4 = Button(root,text="4",padx=50,pady=30, command=lambda : click(4))
button_5 = Button(root,text="5",padx=50,pady=30, command=lambda : click(5))
button_6 = Button(root,text="6",padx=50,pady=30, command=lambda : click(6))
button_7 = Button(root,text="7",padx=50,pady=30, command=lambda : click(7))
button_8 = Button(root,text="8",padx=50,pady=30, command=lambda : click(8))
button_9 = Button(root,text="9",padx=50,pady=30, command=lambda : click(9))
button_0 = Button(root,text="0",padx=50,pady=30, command=lambda : click(0))

button_add = Button(root,text="+",padx=50,pady=30,command=add)
button_sub = Button(root,text="-",padx=50,pady=30,command=sub)
button_mul = Button(root,text="*",padx=50,pady=30,command=mul)
button_div = Button(root,text="/",padx=50,pady=30,command=div)

button_equals = Button(root,text="=",padx=50,pady=30, command=equals)
button_clear = Button(root,text="Clear",padx=50,pady=30, command=lambda : clear())

#Showing on the screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)

button_add.grid(row=4,column=1)
button_sub.grid(row=5,column=0)
button_mul.grid(row=5,column=1)
button_div.grid(row=5,column=2)

button_equals.grid(row=4,column=2)
button_clear.grid(row=4,column=0)

root.mainloop()