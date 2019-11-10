# Calculator-Python
#my first GUI  project in python 


from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=11, padx=10, pady=10)


# function to add the number you have clicked in the box text
def button_click(number):
    current = e.get()
    # this function to delete what is befor in the box
    # try to make it as a commant to understand what i'm saying
    e.delete(0, END)
    # to add in the box what we have as a result
    e.insert(0, str(current) + str(number))


# fun for clear button
def clear_btn():
    e.delete(0, END)


def button_add():
    first_number = e.get()
    global firNum
    global math
    math = "addition"
    firNum = int(first_number)
    e.delete(0, END)

#function for division button
def button_divid():
    first_number = e.get()
    global firNum
    global math
    math = "division"
    firNum = int(first_number)
    e.delete(0, END)

#function for substraction button
def button_sub():
    first_number = e.get()
    global firNum
    global math
    math = "substraction"
    firNum = int(first_number)
    e.delete(0, END)

#function for multiplication button
def button_mult():
    first_number = e.get()
    global firNum
    global math
    math = "multiplication"
    firNum = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, firNum + int(second_number))

    if math == "substraction":
        e.insert(0, firNum - int(second_number))

    if math == "multiplication":
        e.insert(0, firNum * int(second_number))
    if math == "division":
        try:
            e.insert(0, firNum / int(second_number))
        except ZeroDivisionError:
            e.insert(0,'error')
            print('no division by Zero')


# i will use this function to replace all of the buttons in the comment
def lambdaGrid(root, text, padx, pady, command):
    return Button(root, text=text, padx=padx, pady=pady, command=command)


# Define The Buttons

button_1 = lambdaGrid(root, '1', 40, 20, lambda: button_click(1))
button_2 = lambdaGrid(root, '2', 40, 20, lambda: button_click(2))
button_3 = lambdaGrid(root, '3', 40, 20, lambda: button_click(3))
button_4 = lambdaGrid(root, '4', 40, 20, lambda: button_click(4))
button_5 = lambdaGrid(root, '5', 40, 20, lambda: button_click(5))
button_6 = lambdaGrid(root, '6', 40, 20, lambda: button_click(6))
button_7 = lambdaGrid(root, '7', 40, 20, lambda: button_click(7))
button_8 = lambdaGrid(root, '8', 40, 20, lambda: button_click(8))
button_9 = lambdaGrid(root, '9', 40, 20, lambda: button_click(9))
button_0 = lambdaGrid(root, '0', 40, 20, lambda: button_click(0))

"""
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda :button_click(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda :button_click(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda :button_click(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda :button_click(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda :button_click(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda :button_click(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda :button_click(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda :button_click(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda :button_click(9))
button_0 = Button(root, text='0', padx=40, pady=20, command=lambda :button_click(0))
"""
# you can also use the function lambdaGrid to shortcut the code
button_equal = Button(root, text='=', padx=39, pady=20, command=button_equal)
button_clear = Button(root, text='Clear', padx=38, pady=20, command=clear_btn)
button_add = Button(root, text='+', padx=38, pady=20, command=button_add)

button_mul = Button(root, text='*', padx=40, pady=20, command=button_mult)
button_minus = Button(root, text='-', padx=40, pady=20, command=button_sub)
button_div = Button(root, text='/', padx=40, pady=20, command=button_divid)

# Put the buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=1)

button_mul.grid(row=4, column=0)
button_add.grid(row=4, column=3)
button_equal.grid(row=4, column=2)
button_clear.grid(row=1, column=3)
button_minus.grid(row=2, column=3)
button_div.grid(row=3, column=3)

root.mainloop()
