import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# define the name of the file to read from
# filename = "C:/Users/Yorck/Desktop/chat log.txt"
Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

# open the file for reading
file_handle = open(filename, 'r')

while True:
    # read a single line
    line = file_handle.readline()

    if line == "Exit\n":  # Abbruchkriterium
        print(line.strip())
        # break
    if line:
        print(line.strip())
        time.sleep(0.1)
    else:
        time.sleep(0.5)

# close the pointer to that file
file_handle.close()
