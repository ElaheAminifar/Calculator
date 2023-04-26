import tkinter as t
# * means all
from tkinter import *

window = t.Tk()
window.title("Calculator")
window.geometry("300x350")

# main frame inside the window
frame = t.Frame(window)
frame.pack()

# StringVar() is part of * in line 3
equation = StringVar()
expression_field = t.Entry(frame, textvariable=equation)
expression_field.grid(row=1, column=0, columnspan=4)

# defining a function to compute the mathematical operations
def calculate():
    equation.set(eval(equation.get()))

# defining the numbers on the calculator
def c0():
    equation.set(equation.get() + "0")
def c1():
    equation.set(equation.get() + "1")
def c2():
    equation.set(equation.get() + "2")
def c3():
    equation.set(equation.get() + "3")
def c4():
    equation.set(equation.get() + "4")
def c5():
    equation.set(equation.get() + "5")
def c6():
    equation.set(equation.get() + "6")
def c7():
    equation.set(equation.get() + "7")
def c8():
    equation.set(equation.get() + "8")
def c9():
    equation.set(equation.get() + "9")
def c_smile():
    equation.set(equation.get() + " Well done :)")
def c_sum():
    equation.set(equation.get() + "+")
def c_sub():
    equation.set(equation.get() + "-")
def c_mul():
    equation.set(equation.get() + "*")
def c_div():
    equation.set(equation.get() + "/")  # divide by zero?!
def c_dec():
    equation.set(equation.get() + ".")
def c_per():
    equation.set(equation.get() + "*0.01")  # Multiply by 0.01 to find the percentage
def c_ac():
    equation.set("")

def change_sign():
    numbers = equation.get()
    numbers = get_change_sign(numbers)
    equation.set(numbers)

# defining a function with an argument to return
def get_change_sign(numbers):
    if numbers[0] == "-":
        numbers = numbers[1:]
    else:
        numbers = "-"+numbers
    return numbers

# adding buttons for numbers and mathematical operations
cal_btn_ac = t.Button(frame, text='AC', command=c_ac)
cal_btn_ac.grid(row=2, column=0)
cal_btn_sign = t.Button(frame, text='+/-', command=change_sign)
cal_btn_sign.grid(row=2, column=1)
cal_btn_per = t.Button(frame, text='%', command=c_per)
cal_btn_per.grid(row=2, column=2)
cal_btn_div = t.Button(frame, text='÷', command=c_div)
cal_btn_div.grid(row=2, column=3)

cal_btn7 = t.Button(frame, text='7', command=c7)
cal_btn7.grid(row=3, column=0)
cal_btn8 = t.Button(frame, text='8', command=c8)
cal_btn8.grid(row=3, column=1)
cal_btn9 = t.Button(frame, text='9', command=c9)
cal_btn9.grid(row=3, column=2)
cal_btn_mul = t.Button(frame, text='*', command=c_mul)
cal_btn_mul.grid(row=3, column=3)

cal_btn4 = t.Button(frame, text='4', command=c4)
cal_btn4.grid(row=4, column=0)
cal_btn5 = t.Button(frame, text='5', command=c5)
cal_btn5.grid(row=4, column=1)
cal_btn6 = t.Button(frame, text='6', command=c6)
cal_btn6.grid(row=4, column=2)
cal_btn_sub = t.Button(frame, text='-', command=c_sub)
cal_btn_sub.grid(row=4, column=3)

cal_btn1 = t.Button(frame, text='1', command=c1)
cal_btn1.grid(row=5, column=0)
cal_btn2 = t.Button(frame, text='2', command=c2)
cal_btn2.grid(row=5, column=1)
cal_btn3 = t.Button(frame, text='3', command=c3)
cal_btn3.grid(row=5, column=2)
cal_btn_sum = t.Button(frame, text='+', command=c_sum)
cal_btn_sum.grid(row=5, column=3)

cal_btn0 = t.Button(frame, text='0', command=c0)
cal_btn0.grid(row=6, column=0)
cal_btn_smile = t.Button(frame, text=':)', command=c_smile)
cal_btn_smile.grid(row=6, column=1)
cal_btn_dec = t.Button(frame, text='.', command=c_dec)
cal_btn_dec.grid(row=6, column=2)
cal_btn = t.Button(frame, text='=', command=calculate)
cal_btn.grid(row=6, column=3)


window.mainloop()
