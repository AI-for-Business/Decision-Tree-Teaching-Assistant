import tkinter as tk
from tkinter import filedialog as fd
from tkinter import Button, Entry, END, ttk


class GUI:
    def __init__(self):
        # Create main GUI frame
        self.root = tk.Tk()
        self.root.title("DeTTA - Decision Tree Teaching Assistant")
        # self.root.geometry("640x480")

        # Interactive GUI elements
        self.lbl_file_in = None
        self.lbl_path_out = None

        # Create tab control element
        self.tab_control = ttk.Notebook(self.root)
        self.input_tab = self.create_input_tab(self.tab_control)
        self.process_tab = self.create_process_tab(self.tab_control)
        self.tab_control.grid()

        # Start the GUI
        self.root.mainloop()

    def create_input_tab(self, tab_control: ttk.Notebook):
        # Create the frame
        tab = ttk.Frame(tab_control)

        # Todo

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
        c1.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        # Blank line
        l2 = tk.Label(tab, width=0, height=1)
        l2.grid(column=0, row=4)

        # Checkbox Create Solution File
        c2 = tk.Checkbutton(tab, text='Create Solution File')
        c2.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

        # Checkbox Create Graph File
        c4 = tk.Checkbutton(tab, text='Create Graph as PDF')
        c4.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)

        # Checkbox Graph Preview
        c3 = tk.Checkbutton(tab, text='Open Graph Preview')
        c3.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

        # Blank line
        l3 = tk.Label(tab, width=0, height=1)
        l3.grid(column=0, row=7)

        # Checkbox Open output folder
        c5 = tk.Checkbutton(tab, text='Open output folder')
        c5.grid(column=0, row=8, sticky=tk.W, padx=5, pady=5)

        # Button Process Data
        btn_ok = Button(tab, text="Process Data", width=20, command=self.btn_process_data())
        btn_ok.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

        # Button Close
        btn_close = Button(tab, text="Close", width=20, command=self.btn_close)
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

    def choose_output_directory(self):
        folder_selected = fd.askdirectory()
        l = len(folder_selected) + 5
        self.lbl_path_out.config(state='normal')
        self.lbl_path_out.config(width=l)
        self.lbl_path_out.delete(0, END)
        self.lbl_path_out.insert(0, folder_selected)
        self.lbl_path_out.config(state='disabled')

    def btn_close(self):
        self.root.quit()

    def btn_process_data(self):
        # Todo
        pass


# Main Method
if __name__ == '__main__':
    # Todo: Delete this
    g = GUI()
