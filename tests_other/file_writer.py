import os
# save_path = 'D:/'
# file_name = "test.txt"
# completeName = os.path.join(save_path, file_name)
# file = open(completeName, "w")
# file.write("file information")
# file.close()


# Config data
save_path = 'D:/'
file_name = "test"
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
