# Import Module
from tkinter import *


def frame2():
    frame3.grid_remove()
    frame2.grid()


def frame3():
    frame2.grid_remove()
    frame3.grid()


# Create Tkinter Object
root = Tk()

# Set Geometry
root.geometry("400x400")

# Frame 1
frame1 = Frame(root, bg="black", width=500, height=300)
button1 = Button(frame1, text="Switch to Frame 2", command=frame2())
button1.grid()
button2 = Button(frame1, text="Switch to Frame 3", command=frame3())
button2.grid()
frame1.grid()

# Frame 2
frame2 = Frame(frame1, bg="white", width=100, height=100)
frame2.grid(pady=20, padx=20)

# Frame 3
frame3 = Frame(frame1, bg="red", width=100, height=100)
frame3.grid(pady=20, padx=20)
frame3.grid_remove()

# Execute Tkinter
root.mainloop()
