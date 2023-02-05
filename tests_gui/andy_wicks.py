"""
Author: Andy Wicks
Code can be found at: https://lyw4.life/Resources/python.php
Date started: Mon,  19 Oct 2020
Version: 0.0
Purposes:
    - Use frames to hold widgets.
    - Use an entry box to obtain information from the user.
    - Use the information obtained to change another widget.
    Reference: https://pythonbasics.org/tkinter-frame/
    Reference: https://tkdocs.com/tutorial/widgets.html
    Reference: https://tkdocs.com/tutorial/morewidgets.html
    Reference: http://effbot.org/tkinterbook/radiobutton.htm
"""
import tkinter as tk         # This has all the code for GUIs.
import tkinter.font as font  # This lets us use different fonts.


def center_window_on_screen():
    """
    This centres the window when it is not maximised.  It
    uses the screen and window height and width variables
    defined in the program below.
    :return: Nothing
    """
    x_cord = int((screen_width/2) - (width/2))
    y_cord = int((screen_height/2) - (height/2))
    root.geometry("{}x{}+{}+{}".format(width, height, x_cord, y_cord))


def show_message():
    """
    This function shows how frames can be revealed
    and hidden.  Here the message frame is shown
    and the entry frame is hidden.
    :return: Nothing
    """
    message_frame.pack()
    entry_frame.forget()


def show_entry():
    """
    This function shows how frames can be revealed
    and hidden.  Here the entry frame is shown
    and the message frame is hidden.
    :return: Nothing
    """
    entry_frame.pack()
    message_frame.forget()


def show_new_message():
    """
    The wording of the message is "got" from the
    entry box and the label message is then set
    to that.
    :return: Nothing
    """
    msg = entry_entry.get()
    lbl_message.config(text=msg)


# Now we get to the program itself:-
root = tk.Tk()
root.title("An improved GUI")
# Set the icon used for your program
# root.iconphoto(True,
#                tk.PhotoImage(file='info.png'))

# There are three frames being created below.
button_frame = tk.Frame(root)
entry_frame = tk.Frame(root)
message_frame = tk.Frame(root)

# This sets the background colour of the window.
root.configure(bg='lightyellow')

width, height = 500, 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_window_on_screen()

lbl_font = font.Font(family='Georgia', size='18', weight='bold')
txt_font = font.Font(family='Georgia', size='18')
lbl_message = tk.Label(message_frame,
                       text='GUI stands for Graphical\n'
                            'User Interface.  This is a GUI.',
                       font=lbl_font,
                       bg='brown', fg='lightyellow')
lbl_message.pack()

btn_button = tk.Button(button_frame,
                       text="Show/Hide Message",
                       fg='darkred', bg='darkgray',
                       command=show_message)
btn_button.pack(pady=5)
btn_entry = tk.Button(button_frame,
                      text="Show/Hide Enter Message ",
                      fg='darkred', bg='darkgray',
                      command=show_entry)
btn_entry.pack(pady=5)

entry_label = tk.Label(entry_frame,
                       text='Enter the new message in the box below.',
                       font=lbl_font)
entry_label.pack(pady=5)
entry_entry = tk.Entry(entry_frame, font=txt_font)
entry_entry.pack(pady=5)
entry_button = tk.Button(entry_frame,
                         text="Display New Message",
                         fg='darkred', bg='darkgray',
                         command=show_new_message)
entry_button.pack(pady=5)

button_frame.pack(pady=20)
entry_frame.pack(pady=20)
message_frame.pack(pady=10)

root.mainloop()