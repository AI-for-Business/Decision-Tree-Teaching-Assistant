from tkinter import *
from tkinter import ttk


def close():
    root.destroy()


root = Tk()

# Tutorial 1
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
Label1 = Label(root, text="This is too easy", bg="green")
Label1.pack(fill=X)
Label2 = Label(root, text="Label 2", bg="red")
Label2.pack(side=LEFT, fill=Y)
Button1 = Button(topFrame, text="Close", command=close)
Button2 = Button(topFrame, text="Button 2")
Button3 = Button(topFrame, text="Button 3")
Button4 = Button(bottomFrame, text="Button 4")
Button1.pack(side=LEFT)
Button2.pack(side=LEFT)
Button3.pack(side=LEFT)
Button4.pack(side=BOTTOM)
Entry1 = Entry(bottomFrame)
Entry1.pack(side=BOTTOM)

# Tutorial 2
# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
# label_1.grid(row=0, sticky=E)
# label_2.grid(row=1)
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)
#
# c = Checkbutton(root, text="Keep me logged in")
# c.grid(row=2, columnspan=2)
# Button1 = Button(root, text="Close", command=close)
# Button1.grid(row=3, columnspan=2)
#
# # Combobox tryout
# testlist = ["A", "B", "C"]
# comboExample = ttk.Combobox(root, values=testlist)
# comboExample.grid(row=4)

root.mainloop()
