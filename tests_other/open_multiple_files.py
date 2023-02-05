import tkinter.filedialog as fd
from tkinter import *

root = Tk()
filez = fd.askopenfilenames(parent=root, title='Choose a file')
for f in filez:
    print(f)
print(root.tk.splitlist(filez))


# Just to check that 'break' works
# for a in range(10):
#     if a > 5:
#         print("End")
#         break
#     else:
#         print(a)
