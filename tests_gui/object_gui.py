from tkinter import *
import tkinter as tk
from tkinter import ttk


class Gui:
    def __init__(self):
        self.all_frames = []
        self.statusbar = ()

        # Setup the GUI
        root = Tk()
        root.title("Internet-of-Things Simulation Engine (IoTSE) ALPHA GUI")
        # root.iconbitmap('/path/to/ico/icon.ico')

        # Version 1: Fixed starting size
        root.geometry("640x480")

        # Version 2: Starting size = max screen resolution
        # screen_width = root.winfo_screenwidth()
        # screen_height = root.winfo_screenheight()
        # root.geometry(str(screen_width)+'x'+str(screen_height))

        # Version 3: Fullscreen without Title Bar
        # root.attributes("-fullscreen", True)

        # Create a menu bar
        menubar = Menu(root)

        # 'File' sub menu bar
        filemenu = Menu(menubar, tearoff=False)
        filemenu.add_command(label="New Scenario...", accelerator="Ctrl+N")
        filemenu.add_command(label='Load Scenario...', underline=0, accelerator="Ctrl+L")
        filemenu.add_command(label='Save Scenario', underline=0, accelerator="Ctrl+S")
        filemenu.add_command(label='Save Scenario As...', underline=15, accelerator="Ctrl+A")
        filemenu.add_separator()
        filemenu.add_command(label='Exit', underline=1, command=root.quit)
        menubar.add_cascade(label='File', underline=0, menu=filemenu)

        # 'Edit' sub menu bar
        editmenu = Menu(menubar, tearoff=False)
        editmenu.add_command(label="Copy", underline=0)
        editmenu.add_command(label='Paste', underline=0)
        editmenu.add_separator()
        editmenu.add_command(label='Cut', underline=2)
        editmenu.add_command(label='Undo', underline=0)
        menubar.add_cascade(label='Edit', underline=0, menu=editmenu)

        # Finalize menu bar
        root.config(menu=menubar)

        # Create the various frames used by the GUI
        self.create_frames(root)

        # Create the status bar (bottom) for shared use
        self.create_statusbar(root)

        # Show the GUI
        mainloop()

    def create_frames(self, r):
        self.create_frame0(r)
        self.hide_all_frames()

    def create_frame0(self, r):
        # This frame is an empty frame, used for the first visit. It contains no information or functionality.
        frame0 = Frame(r)
        frame0.pack()
        btn1 = Button(frame0, text="Do Nothing")  # To show something happened ...
        btn1.pack()  # To show something happened ...
        self.all_frames.append(frame0)

    def hide_all_frames(self):
        for f in self.all_frames:
            f.forget()

    def create_statusbar(self, r):
        frame_statusbar = Frame(r)
        label_statusbar = Label(frame_statusbar, text="Statusbar initialized...", anchor=W, height=2, relief=SUNKEN)
        label_statusbar.pack(fill="x", expand="true", side=LEFT)
        label_status_time = Label(frame_statusbar, text="Hallo Du liebe weite Welt", anchor=E, height=2, relief=SUNKEN)
        label_status_time.pack(side=LEFT)
        frame_statusbar.pack(side=BOTTOM, fill="x")
        # Just for debugging reasons:
        # frame_statusbar.config(bg="red")
        # label_statusbar.config(bg="yellow")
        # label_status_time.config(bg="blue")
        self.statusbar = frame_statusbar


if __name__ == "__main__":
    g = Gui()
