import tkinter
from tkinter import *


def ok_button():
    if text.get() == "":
        print("OK Button pressed")
    else:
        print(text.get())


def close_button():
    root.quit()


He = 700
Wi = 800

root = Tk()
canvas = tkinter.Canvas(root, height=He, width=Wi)
label1 = Label(root, text="enter something")
text = Entry()
button1 = Button(text="OK", command=ok_button)
button2 = Button(text="Close", command=close_button)

canvas.pack()
label1.pack()
text.pack()
button1.pack()
button2.pack()

root.mainloop()


