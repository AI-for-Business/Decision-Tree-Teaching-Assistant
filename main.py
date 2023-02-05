import pandas as pd
import subprocess
import gui
import tkinter.filedialog as fd  # Open multiple files
import os  # file writer
from tkinter import Tk  # Ask filename
from tkinter.filedialog import askopenfilename  # Ask filename


# Read data from a file and convert it into a pandas dataset
def read_data_set(path: str) -> pd.DataFrame:
    with open(path, 'r') as f:  # Open the file
        data = f.readlines()  # Read the file entries
    for i in range(len(data)):
        data[i] = data[i].split(";")  # Split the rows by semi-colons
    dataset = pd.DataFrame(data)  # Encapsulate in a dataframe
    dataset = dataset.replace(r'\n', '', regex=True)  # Remove '\n' character
    cols = dataset.iloc[0]  # Get the column labels
    dataset = dataset.iloc[1:, :]  # Drop first row (the labels)
    dataset.columns = cols  # Set the first row as column labels
    return dataset


# Read data from a CSV file
def read_csv_file(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


# Read data from a Tab-Separated-Values file
def read_tsv_file(path: str) -> pd.DataFrame:
    return pd.read_csv(path, delimiter='\t')


# Open Windows Explorer on the output folder
def jump_to_folder() -> None:
    subprocess.Popen(r'explorer "C:\Users\yorck\Downloads"')


# ======== Supporting Functions ========


# Open multiple files:
def open_multiple_files():
    root = Tk()
    files = fd.askopenfilenames(parent=root, title='Choose a file')
    for f in files:
        print(f)
    print(root.tk.splitlist(files))


# File Writer:
def file_writer():
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


# define the name of the file to read from
def ask_filename():
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file

    # open the file for reading
    file_handle = open(filename, 'r')

    # close the pointer to that file
    file_handle.close()


# Based on a pandas dataframe, a decision tree will be calculated
def calculate_data(data: pd.DataFrame):
    print(data.to_string())


# Drawing a decision tree as PDF-File
def visualize_data():
    pass


def test_subsets(ds: pd.DataFrame):
    candidates: list[str] = []

    # print("=== Original dataset:")
    # print(ds)

    # print("=== Dropping first column:")
    # candidates.append('Aussicht')
    # print(ds.drop(columns=candidates))
    # print("=== Dropping second column:")
    # candidates.append('Wind')
    # print(ds.drop(columns=candidates))
    # print("=== Dropping last two rows:")
    # print(ds.drop(index=('Aussicht', 'Bedeckt')))  # Does not work

    # Get dataset column headers
    # print(ds.columns.to_list())
    # x = ds.columns.to_list()
    # print(x[1])

    # Print first 5 items of column Aussicht
    # print(ds['Aussicht'][0:5])

    # Print first 5 items of columns Aussicht and Wind
    # print(ds[['Aussicht', 'Wind']][0:5])

    # Print a single row by its index
    # print(ds.iloc[0])

    # Print multiple rows by their index
    # print(ds.iloc[1:4])

    # Read a specific location (R, C)
    # print(ds.iloc[2, 0])

    # Ready every value separately
    # for index, row in ds.iterrows():
    #     print(index, row)

    # Select all rows that have a certain value in a certain column
    # col = "Feuchtigkeit"
    # row = "Hoch"
    # print(ds.loc[ds[col] == row])

    # Get all different values of a column

    # Count each distinct value's count

    # Sort dataset by a given column
    print(ds.sort_values(['Aussicht', 'Wind'], ascending=True))

    # Get high-level statistical data about the dataset
    # print(ds.describe())


# Main Method: This is where you start the Decision Tree Teaching Assistant
if __name__ == '__main__':
    df1 = read_data_set('C:/Users/yorck/Downloads/DeTTA-Data/tennis.csv')
    print(df1)

    # df2 = pd.read_csv('C:/Users/yorck/Downloads/tennis.csv')
    # print(df2.to_string())
    # test_subsets(df2)

    # df3 = pd.DataFrame(df2, columns=['Pulse'])
    # print(df3)

    # jump_to_folder()
    # gui.start_gui()
    # g = gui.GUI()
    pass
