import os
from datetime import datetime, timedelta
from tkinter import filedialog
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory()
print(folder_selected)

d1 = datetime.now()
y = d1.year
mo = d1.month
d = d1.day
h = d1.hour
mi = d1.minute
s = d1.second

save_path = folder_selected
file_name = "Sensor_Event_Log_" + str(y) + "." + str(mo) + "." + str(d) + "-" + str(h) + "." + str(mi) + "." + str(s)
file_ending = ".txt"

# Creating filenames for true and noisy sensor logs
f1n = file_name + file_ending
f2n = file_name + "_noise" + file_ending
name_true = os.path.join(save_path, f1n)
name_noise = os.path.join(save_path, f2n)

# Write true event log to file
file1 = open(name_true, "w")
file1.write("file information")
file1.close()

# Write noisy event log to file
file2 = open(name_noise, "w")
file2.write("file information")
file2.close()
