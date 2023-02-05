import tkinter as tk
from tkinter import *
from tkinter import ttk


def frame2():
    frame2.pack()
    frame3.forget()


def frame3():
    frame3.pack()
    frame2.forget()


def close_all_frames():
    frame2.forget()
    frame3.forget()


def pop_up_message():
    popup = tk.Tk()
    popup.wm_title("!")
    norm_font = ("Verdana", 10)
    message_text = "Hallo, dies ist ein Popup"
    label = ttk.Label(popup, text=message_text, font=norm_font)
    label.pack(side="top", fill="x", pady=10)
    e1 = Entry()
    e1.pack()
    b1 = ttk.Button(popup, text="Close", command=popup.destroy)
    b1.pack()
    b2 = ttk.Button(popup, text="Save")
    b2.pack()
    popup.mainloop()


def create_menu():
    # 'File' sub menu bar
    file_menu = Menu(menu_bar, tearoff=False)
    file_menu.add_command(label="New File", accelerator="Ctrl+Q")
    # file_menu.bind("<Ctrl-Q>", tk.close_all_frames)
    # root.bind_all("<Control-q>", root.close_all_frames)
    file_menu.add_command(label='Open File', command=pop_up_message)
    file_menu.add_command(label='Save')
    file_menu.add_command(label='Save As')
    file_menu.add_separator()
    file_menu.add_command(label='Exit', command=root.quit)
    menu_bar.add_cascade(label='File', underline=0, menu=file_menu)

    # 'Edit' sub menu bar
    edit_menu = Menu(menu_bar, tearoff=False)
    edit_menu.add_command(label="Copy", underline=0)
    edit_menu.add_command(label='Paste', underline=0)
    edit_menu.add_separator()
    edit_menu.add_command(label='Cut', underline=0)
    edit_menu.add_command(label='Undo', underline=0)
    menu_bar.add_cascade(label='Edit', underline=0, menu=edit_menu)

    # Finalize menu bar
    root.config(menu=menu_bar)
    root.bind_all("<Control-q>", close_all_frames)


# Create Tkinter Object
root = Tk()
root.title("Internet-of-Things Simulation Engine (IoTSE) ALPHA GUI")
# root.iconbitmap('/path/to/ico/icon.ico')
root.geometry("400x400")

# Create a menu bar
menu_bar = Menu(root)
create_menu()

# Frame 0, status bar at bottom, always present

# Frame 1, empty starting frame, only present on first visit

# Frame 1, always present
frame1 = Frame(root, bg="black", width=500, height=300, highlightbackground="black", highlightthickness=1)
button1 = Button(frame1, width=20, text="Switch to Frame 2", command=frame2)
button2 = Button(frame1, width=20, text="Switch to Frame 3", command=frame3)
button3 = Button(frame1, width=20, text="Close all frames", command=close_all_frames)
button4 = Button(frame1, width=20, text="Quit Application", command=root.quit)
button5 = Button(frame1, width=20, text="Start Pop-Up", command=pop_up_message)
status_bar = Label(width=500, text="", relief=SUNKEN)
status_bar.pack()
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
frame1.pack()

# Frame 2, exchangeable
frame2 = Frame(frame1, bg="white", width=100, height=100)
frame2.pack(pady=20, padx=20)
frame2.forget()

# Frame 3, exchangeable
frame3 = Frame(frame1, bg="red", width=100, height=100)
frame3.pack(pady=20, padx=20)
frame3.forget()

# Execute Tkinter
root.mainloop()
