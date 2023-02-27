from tkinter import filedialog as fd
from tkinter import Button, Entry, END, ttk, Label, IntVar
from os import path
from datetime import datetime
from numpy import random as r
import tkinter as tk
import typing
import generator as g
# import solver as s


class GUI:
    def __init__(self):
        # Create main GUI frame
        self.root = tk.Tk()
        # self.root.geometry("640x480")
        # self.root.config(background='blue')
        self.root.title("DeTTA - Decision Tree Teaching Assistant")

        # Interactive GUI elements
        self.lbl_file_in = None
        self.lbl_path_out = None
        self.lbl_path_data_out = None
        self.Columns: Entry = None
        self.Rows: Entry = None
        self.Values: Entry = None

        # Create tab control element
        self.tab_control = ttk.Notebook(self.root)
        self.input_tab = self.create_input_tab(self.tab_control)
        self.process_tab = self.create_process_tab(self.tab_control)
        self.tab_control.grid()

        # Filehandler for data generation
        self.output_file: typing.TextIO | None = None

        # Start the GUI
        self.root.mainloop()

    def create_input_tab(self, tab_control: ttk.Notebook):
        # Create the frame
        tab = ttk.Frame(tab_control)
        tab.columnconfigure(0, weight=1)
        tab.columnconfigure(1, weight=1)

        lbl_cols = Label(tab, text="Amount of columns:")
        lbl_cols.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        ent_cols = Entry(tab, width=50)
        ent_cols.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        self.Columns = ent_cols

        lbl_vals = Label(tab, text="Different values per column:")
        lbl_vals.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        ent_vals = Entry(tab, width=50)
        ent_vals.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
        self.Columns = ent_vals

        lbl_rows = Label(tab, text="Amount of rows:")
        lbl_rows.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        ent_rows = Entry(tab, width=50)
        ent_rows.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        self.Columns = ent_rows

        btn_output_data = Button(tab, text="Choose data output directory", command=self.choose_data_output_directory)
        btn_output_data.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        lbl_path_data_out = Entry(tab, width=50, state='disabled')
        lbl_path_data_out.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
        self.lbl_path_data_out = lbl_path_data_out

        l1 = tk.Label(tab, width=0, height=1)
        l1.grid(column=0, row=4)

        var6 = IntVar()
        var6.set(0)
        c6 = tk.Checkbutton(tab, text='Open Folder', variable=var6)
        c6.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

        # btn_create_data = Button(tab, text="Create data...", command=self.create_tennis_data)
        btn_create_data = Button(tab, text="Create data...", command=g.create_data(ent_cols.get(), ent_vals.get(), ent_rows.get(), lbl_path_data_out, c6.getvar))
        btn_create_data.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

        # Add the frame to the frame tab controller
        tab_control.add(tab, text="Input Data")
        return tab

    def create_process_tab(self, tab_control: ttk.Notebook):
        # Create the frame
        tab = ttk.Frame(tab_control)
        tab.columnconfigure(0, weight=1)
        tab.columnconfigure(1, weight=1)

        # Input data to process
        btn_input = Button(tab, text="Choose input file...", command=self.choose_input_file)
        btn_input.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        lbl_file_in = Entry(tab, width=50, state='disabled')
        lbl_file_in.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        self.lbl_file_in = lbl_file_in

        # Blank line
        l0 = tk.Label(tab, width=0, height=1)
        l0.grid(column=0, row=1)

        # Output directory
        btn_output = Button(tab, text="Choose output directory...", command=self.choose_output_directory)
        btn_output.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        lbl_path_out = Entry(tab, width=50, state='disabled')
        lbl_path_out.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        self.lbl_path_out = lbl_path_out

        # Checkbox create files in sub folder
        c1 = tk.Checkbutton(tab, text='Create files in sub folder')
        c1.select()
        c1.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        # Blank line
        l2 = tk.Label(tab, width=0, height=1)
        l2.grid(column=0, row=4)

        # Checkbox Create Solution File
        c2 = tk.Checkbutton(tab, text='Create Solution File')
        c2.select()
        c2.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

        # Checkbox Create Graph File
        c3 = tk.Checkbutton(tab, text='Create Graph as PDF')
        c3.select()
        c3.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)

        # Checkbox Graph Preview
        c4 = tk.Checkbutton(tab, text='Open Graph Preview')
        c4.select()
        c4.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

        # Blank line
        l3 = tk.Label(tab, width=0, height=1)
        l3.grid(column=0, row=7)

        # Checkbox Open output folder
        c5 = tk.Checkbutton(tab, text='Open output folder')
        c5.select()
        c5.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)

        # Button Process Data
        btn_ok = Button(tab, text="Process Data", width=20, command=self.btn_process_data)
        btn_ok.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

        # Button Close
        btn_close = Button(tab, text="Quit", width=20, command=self.btn_close)
        btn_close.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)

        # Add the frame to the frame tab controller
        tab_control.add(tab, text="Process Data")
        return tab

    def choose_input_file(self):
        file_selected = fd.askopenfilename()
        l = len(file_selected) + 5
        self.lbl_file_in.config(state='normal')
        self.lbl_file_in.config(width=l)
        self.lbl_file_in.delete(0, END)
        self.lbl_file_in.insert(0, file_selected)
        self.lbl_file_in.config(state='disabled')

    def set_input_file(self, file):
        l = len(file) + 5
        self.lbl_file_in.config(state='normal')
        self.lbl_file_in.config(width=l)
        self.lbl_file_in.delete(0, END)
        self.lbl_file_in.insert(0, file)
        self.lbl_file_in.config(state='disabled')
        self.set_output_directory(file)

    def choose_output_directory(self):
        folder_selected = fd.askdirectory()
        l = len(folder_selected) + 5
        self.lbl_path_data_out.config(state='normal')
        self.lbl_path_data_out.config(width=l)
        self.lbl_path_data_out.delete(0, END)
        self.lbl_path_data_out.insert(0, folder_selected)
        self.lbl_path_data_out.config(state='disabled')

    def choose_data_output_directory(self):
        folder_selected = fd.askdirectory()
        l = len(folder_selected) + 5
        self.lbl_path_data_out.config(state='normal')
        self.lbl_path_data_out.config(width=l)
        self.lbl_path_data_out.delete(0, END)
        self.lbl_path_data_out.insert(0, folder_selected)
        self.lbl_path_data_out.config(state='disabled')

    def set_output_directory(self, file):
        filepath = path.dirname(file)
        l = len(filepath) + 5
        self.lbl_path_out.config(state='normal')
        self.lbl_path_out.config(width=l)
        self.lbl_path_out.delete(0, END)
        self.lbl_path_out.insert(0, filepath)
        self.lbl_path_out.config(state='disabled')

    def btn_close(self):
        self.root.quit()

    def btn_process_data(self):
        # Todo Create method 'process data'
        pass

    def create_tennis_data(self):
        save_path: str = "C:/Users/Yorck Zisgen/Downloads"  # Get file path from user input via configuration manager

        # Create file name from current timestamp
        d1: datetime = datetime.now()
        y: str = str(d1.year)
        mo: str = self.convert(d1.month)
        d: str = self.convert(d1.day)
        h: str = self.convert(d1.hour)
        mi: str = self.convert(d1.minute)
        s: str = self.convert(d1.second)

        # File name
        file_name: str = "Data_" + y + "." + mo + "." + d + "-" + h + "." + mi + "." + s + ".csv"

        # Creating file names for valid and noisy sensor logs and trace log
        fn: str = path.join(save_path, file_name)  # Create file handler
        self.output_file = open(fn, "w")

        outlook = ["Sunny", "Overcast", "Rainy"]
        temp = ["Hot", "Mild", "Cool"]
        humidity = ["High", "Normal"]
        windy = ["True", "False"]
        s: str = "Outlook;Temp;Humidity;Windy;Play;\n"
        self.output_file.write(s)

        for i in range(100):
            o = outlook[r.randint(0, len(outlook))]
            t = temp[r.randint(0, len(temp))]
            h = humidity[r.randint(0, len(humidity))]
            w = windy[r.randint(0, len(windy))]

            if o == "Overcast":
                p = "Yes"
            elif o == "Rainy" and w == "False":
                p = "Yes"
            elif o == "Sunny" and h == "Normal":
                p = "Yes"
            else:
                p = "No"

            # p = self.tree1(o, t, h, w)

            s: str = o + ";" + t + ";" + h + ";" + w + ";" + p + "\n"
            self.output_file.write(s)

        self.output_file.close()
        self.set_input_file(self.output_file.name)

    @staticmethod
    def convert(val: int) -> str:
        """
        Methods converts an integer to a string, adding a preceding zero if the integer is single-digit
        :param val: Integer value to be converted, e.g. '5' or '12'
        :return: A two-digit string, e.g. '05' or '12'.
        """
        # Add a leading zero to values below 10 for a uniform appearance of file names
        if val < 10:
            val = "0" + str(val)
        else:
            val = str(val)
        return val

    @staticmethod
    def tree1(o, t, h, w):
        if o == "Overcast":
            p = "Yes"
        elif o == "Rainy" and w == "False":
            p = "Yes"
        elif o == "Sunny" and h == "Normal":
            p = "Yes"
        else:
            p = "No"

        return p

    @staticmethod
    def tree2(o, t, h, w):
        columns = ["Outlook", "Temp", "Humidity", "Windy"]
        outlook = ["Sunny", "Overcast", "Rainy"]
        temp = ["Hot", "Mild", "Cool"]
        humidity = ["High", "Normal"]
        windy = ["True", "False"]
        pass


# Main Method
if __name__ == '__main__':
    # Todo: Delete this
    g = GUI()
