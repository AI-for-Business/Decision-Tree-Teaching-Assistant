from tkinter import *


def add():
    if entry1.index("end") == 0:
        pass
    else:
        a = entry1.get()
        listbox.insert("end", a)


root = Tk()
root.geometry("300x320")
frame1 = Frame(root)
frame1.pack(side=LEFT)
frame2 = Frame(root)
frame2.pack(side=RIGHT)
label1 = Label(frame1, text="A list of Grocery items.")
label1.pack()

listbox = Listbox(frame1, selectmode="multiple")
listbox.pack(side=LEFT, fill=BOTH)

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.insert(1, "Bread")
listbox.insert(2, "Milk")
listbox.insert(3, "Meat")
listbox.insert(4, "Cheese")
listbox.insert(5, "Vegetables")

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry1 = Entry(frame2)
entry1.pack()
btn1 = Button(frame2, text="Add to Listbox", command=add)
btn1.pack()
btn3 = Button(frame2, text="Close", command=root.quit)
btn3.pack()


root.mainloop()
