from tkinter import *


def set_text():
    if entry1.index("end") == 0:
        pop_up_error()
    else:
        label1.config(text=entry1.get())


def pop_up_error():
    popup = Tk()
    popup.wm_title("!")
    norm_font = ("Verdana", 10)
    message_text = "Hallo, dies ist ein Popup"
    label_x = Label(popup, text=message_text, font=norm_font)
    label_x.pack(side="top", fill="x", pady=10)
    b1 = Button(popup, text="Close", command=popup.destroy)
    b1.pack()
    popup.mainloop()


def open_window():
    global entry1
    top = Toplevel()
    top.geometry("200x200+500+100")
    my_label = Label(top, text="Please enter some text")
    my_label.pack()
    entry1 = Entry(top, width=50)
    entry1.pack()
    btn3 = Button(top, text="Set Text", command=set_text)
    btn3.pack()
    btn4 = Button(top, text="Close", command=top.destroy)
    btn4.pack()
    top.mainloop()


global label1
global entry1
root = Tk()
root.geometry("200x200")
btn1 = Button(root, text="Open second window", command=open_window)
btn1.pack()
btn2 = Button(text="Close", command=root.destroy)
btn2.pack()
label1 = Label(root, text="demo")
label1.pack()
root.mainloop()
