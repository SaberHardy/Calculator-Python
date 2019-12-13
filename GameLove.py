from tkinter import *
from tkinter import messagebox

from PIL import Image,ImageTk

root = Tk()
root.title('LoveApp')
#root.geometry('400x400')
LoverGame=LabelFrame(root,text='He/She Loves You ?',font='Helvetica 13 bold',fg='#ff0000',padx=10,pady=10)
LoverGame.grid(padx=10, pady=10)

labelName = Label(LoverGame,text="Your Name",font='Helvetica 9 bold').grid(row=0, column=0, sticky=W)
loverName = Label(LoverGame,text="Lover Name",font='Helvetica 9 bold').grid(row=1, column=0, sticky=W)

NameEntry=Entry(LoverGame, bd=1, bg="white", highlightbackground="#bebebe", highlightthickness=1)
NameEntry.grid(row=0, column=1, pady=3,ipady=1)

loverName=Entry(LoverGame, bd=1, bg="white", highlightbackground="#bebebe", highlightthickness=1)
loverName.grid(row=1, column=1, pady=3, ipady=1)


def sumOfDigits(num):
    sum =0
    while num>0:
        sum+=(num%10)
        num/=10
    return sum

mylbl=Label(LoverGame)
#mylbl.place(x=145,y=73)
def calculateLove():
    global mylbl
    mylbl.grid_forget()

    name=NameEntry.get()
    name.lower()
    namelen=len(name)

    love=loverName.get()
    love.lower()
    lovelen = len(love)

    if name =='' or love=='':
        messagebox.showwarning('Warning','Sorry! one of fields is empty!')
    else:
        calculatepercent = (sumOfDigits(namelen) + sumOfDigits(lovelen)) + 40
        if calculatepercent >= 100:
            calculatepercent = 100

        locationimage = Image.open("F:\\heart.png")
        render = ImageTk.PhotoImage(locationimage)
        img = Label(image=render)
        img.image = render
        img.place(x=210, y=110)

        mylbl = Label(LoverGame, text="%.2f" % calculatepercent + "%")
        mylbl.place(x=145, y=73)



lablresult= Label(LoverGame, text="Loves you " ,font='Helvetica 9 bold').grid(row=2, column=1, sticky=W)

calculateBtn = Button(LoverGame,text='Calculate',font='bold',command=calculateLove)
calculateBtn.grid(row=2,column=0,pady=7,ipady=3, sticky=W)

root.mainloop()
