from tkinter import *


def hello():
    b = a.get()
    myLabel3 = Label(ss, text=b, fg='red', bg='yellow', font=10).pack()


def delete():
    myLabel1 = Label(myGui, text='deleted', fg='red', bg='yellow', font=10).pack()


myGui = Tk()
myGui.title("Hello")
myGui.geometry("400x400+100+50")

ss = Tk()
ss.title("Second Window")
ss.geometry("400x400+600+50")

a = StringVar()


myLabel1 = Label(myGui, text='label one', fg='red', bg='yellow', font=10).pack()
myButton1 = Button(myGui, text='enter', fg='black', bg='green', command=hello, font=10).pack()
myButton2 = Button(ss, text='delete', fg='black', bg='red', command=delete, font=20).pack()
text = Entry(myGui, textvariable=a).pack()

myGui.mainloop()
ss.mainloop()
