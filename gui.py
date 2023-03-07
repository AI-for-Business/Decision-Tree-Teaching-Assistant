import os.path
from tkinter import filedialog as fd
from tkinter import Button, Entry, END, ttk, Label
import tkinter as tk
import typing
import generator as g
import solver as s


class GUI:
    def __init__(self):
        # Create main GUI frame
        self.root = tk.Tk()
        # self.root.geometry("640x480")
        # self.root.config(background='blue')
        self.root.title("DeTTA - Decision Tree Teaching Assistant")

        # Interactive GUI elements
        self.lbl_file_in = None
        self.lbl_file_in_val = None
        self.lbl_path_out = None
        self.lbl_path_out_val = None
        self.lbl_path_data_out = None
        self.Columns: Entry | None = None
        self.Rows: Entry | None = None
        self.Values: Entry | None = None

        # Create tab control element
        self.tab_control = ttk.Notebook(self.root)
        self.input_tab = self.create_input_tab(self.tab_control)
        self.process_tab = self.create_process_tab(self.tab_control)
        self.tab_control.grid()

        # Filehandler for data generation
        self.output_file: typing.TextIO | None = None

        # Start the GUI
        self.root.mainloop()

    def create_input_tab(self, tab_control: ttk.Notebook) -> tk.Frame:
        """
        Creates the input tab.
        :param tab_control: The main menu of the program.
        """
        # Create the frame
        tab = ttk.Frame(tab_control)
        tab.columnconfigure(0, weight=1)
        tab.columnconfigure(1, weight=1)

        # amount of columns
        lbl_cols = Label(tab, text="Amount of columns:")
        lbl_cols.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        ent_cols_val = tk.IntVar()
        ent_cols = Entry(tab, width=50, textvariable=ent_cols_val)
        ent_cols.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        self.Columns = ent_cols

        # different values per column
        lbl_vals = Label(tab, text="Different values per column:")
        lbl_vals.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        ent_vals_val = tk.IntVar()
        ent_vals = Entry(tab, width=50, textvariable=ent_vals_val)
        ent_vals.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
        self.Columns = ent_vals

        # amount of rows
        lbl_rows = Label(tab, text="Amount of rows:")
        lbl_rows.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        ent_rows_val = tk.IntVar()
        ent_rows = Entry(tab, width=50, textvariable=ent_rows_val)
        ent_rows.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        self.Columns = ent_rows

        # data output directory
        btn_output_data = Button(tab, text="Choose data output directory", command=self.choose_data_output_directory)
        btn_output_data.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
        lbl_path_data_out_val = tk.StringVar()
        lbl_path_data_out = Entry(tab, width=50, state='disabled', textvariable=lbl_path_data_out_val)
        lbl_path_data_out.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)
        self.lbl_path_data_out = lbl_path_data_out

        # blank line
        l1 = tk.Label(tab, width=0, height=1)
        l1.grid(column=0, row=4)

        def create_data_action() -> tk.Frame | None:
            """
            What happens after the "create data" button is pressed.
            :return: A Frame if data is created and None if invalid input parameters are given.
            """

            # nothing happens with invalid input
            if ent_cols_val.get() <= 0 or ent_vals_val.get() <= 0 or ent_rows_val.get() <= 0 or \
                    lbl_path_data_out_val.get() == "":
                return

            # create data
            data_path = g.create_data(ent_cols_val.get(), ent_vals_val.get(), ent_rows_val.get(),
                                      lbl_path_data_out_val.get())

            # go to process data tab and set the input file and output directory
            self.tab_control.select(self.process_tab)
            self.lbl_file_in_val.set(data_path)
            self.lbl_path_out_val.set(lbl_path_data_out_val.get())

        # create data button
        btn_create_data = Button(tab, text="Create data...", command=create_data_action)
        btn_create_data.grid(column=1, row=5, sticky=tk.W, padx=5, pady=5)

        # Add the frame to the frame tab controller
        tab_control.add(tab, text="Input Data")
        return tab

    def create_process_tab(self, tab_control: ttk.Notebook) -> tk.Frame:
        """
        Creates the process tab.
        :param tab_control: The main menu of the program.
        :return: The created frame.
        """
        # Create the frame
        tab = ttk.Frame(tab_control)
        tab.columnconfigure(0, weight=1)
        tab.columnconfigure(1, weight=1)

        # Input data to process
        btn_input = Button(tab, text="Choose input file...", command=self.choose_input_file)
        btn_input.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        lbl_file_in_val = tk.StringVar()
        lbl_file_in = Entry(tab, width=50, state='disabled', textvariable=lbl_file_in_val)
        lbl_file_in.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
        self.lbl_file_in_val = lbl_file_in_val
        self.lbl_file_in = lbl_file_in

        # Blank line
        l0 = tk.Label(tab, width=0, height=1)
        l0.grid(column=0, row=1)

        # Output directory
        btn_output = Button(tab, text="Choose output directory...", command=self.choose_output_directory)
        btn_output.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
        lbl_path_out_val = tk.StringVar()
        lbl_path_out = Entry(tab, width=50, state='disabled', textvariable=lbl_path_out_val)
        lbl_path_out.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
        self.lbl_path_out_val = lbl_path_out_val
        self.lbl_path_out = lbl_path_out

        # Checkbox create files in sub folder
        c1_val = tk.BooleanVar()
        c1 = tk.Checkbutton(tab, text='Create files in sub folder', variable=c1_val)
        c1.select()
        c1.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)

        # Blank line
        l2 = tk.Label(tab, width=0, height=1)
        l2.grid(column=0, row=4)

        # Checkbox Create detailed Solution File
        c2_val = tk.BooleanVar()
        c2 = tk.Checkbutton(tab, text='Create Detailed Solution File', variable=c2_val)
        c2.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)

        def toggle_cb_graph_preview() -> None:
            """
            Displays the checkbox for the graph preview when c3 is checked.
            """
            if not c3_val.get():
                c4.grid_remove()
            else:
                c4.grid()

        # Checkbox Create Graph File
        c3_val = tk.BooleanVar()
        c3 = tk.Checkbutton(tab, text='Create Graph as SVG', variable=c3_val, command=toggle_cb_graph_preview)
        c3.select()
        c3.grid(column=0, row=6, sticky=tk.W, padx=5, pady=5)

        # Checkbox Graph Preview
        c4_val = tk.BooleanVar()
        c4 = tk.Checkbutton(tab, text='Open Graph Preview', variable=c4_val)
        c4.select()
        c4.grid(column=1, row=6, sticky=tk.W, padx=5, pady=5)

        # Checkbox DOT file
        c5_val = tk.BooleanVar()
        c5 = tk.Checkbutton(tab, text="Create DOT file", variable=c5_val)
        c5.grid(column=0, row=7, sticky=tk.W, padx=5, pady=5)

        # Button Process Data
        btn_ok = Button(tab, text="Process Data", width=20, command=lambda: s.process_data(lbl_file_in_val.get(),
                                                                                           c2_val.get(),
                                                                                           lbl_path_out_val.get(),
                                                                                           c3_val.get(), c4_val.get(),
                                                                                           c5_val.get(), c1_val.get()))
        btn_ok.grid(column=1, row=8, sticky=tk.W, padx=5, pady=5)

        # Button Close
        btn_close = Button(tab, text="Quit", width=20, command=lambda: self.btn_close(c3_val.get(), c4_val.get(),
                                                                                      c1_val.get()))  # see the def of
        # btn_close() on why it has arguments
        btn_close.grid(column=1, row=9, sticky=tk.W, padx=5, pady=5)

        # Add the frame to the frame tab controller
        tab_control.add(tab, text="Process Data")
        return tab

    def choose_input_file(self):
        """
        The command which is executed after the button for choosing the input file is pressed.
        The file system is displayed and the user selects the input file. After that the directory for the output
        is automatically set as the same directory as the input file directory.
        """

        # select the input file
        file_selected = fd.askopenfilename()
        file_selected_len = len(file_selected) + 5
        self.lbl_file_in.config(state='normal')
        self.lbl_file_in.config(width=file_selected_len)
        self.lbl_file_in.delete(0, END)
        self.lbl_file_in.insert(0, file_selected)
        self.lbl_file_in.config(state='disabled')

        # set the output directory
        file_name_len = len(os.path.basename(file_selected))
        output_dir = file_selected[:-(file_name_len+1)]
        output_dir_len = len(output_dir) + 5
        self.lbl_path_out.config(state='normal')
        self.lbl_path_out.config(width=output_dir_len)
        self.lbl_path_out.delete(0, END)
        self.lbl_path_out.insert(0, output_dir)
        self.lbl_path_out.config(state='disabled')

    def choose_output_directory(self):
        """
        The command which is executed after the button for choosing the output directory of the processed files is
        pressed. The file system is displayed and the user selects the output directory.
        """
        folder_selected = fd.askdirectory()
        length = len(folder_selected) + 5
        self.lbl_path_out.config(state='normal')
        self.lbl_path_out.config(width=length)
        self.lbl_path_out.delete(0, END)
        self.lbl_path_out.insert(0, folder_selected)
        self.lbl_path_out.config(state='disabled')

    def choose_data_output_directory(self):
        """
        The command which is executed after the button for choosing the output directory for the generated data file
        is pressed. The file system is displayed and the user selects the output directory.
        """
        folder_selected = fd.askdirectory()
        length = len(folder_selected) + 5
        self.lbl_path_data_out.config(state='normal')
        self.lbl_path_data_out.config(width=length)
        self.lbl_path_data_out.delete(0, END)
        self.lbl_path_data_out.insert(0, folder_selected)
        self.lbl_path_data_out.config(state='disabled')

    def btn_close(self, c3_dummy: bool, c4_dummy: bool, c1_dummy: bool):
        """
        The command for the close button. For some reason the select() method for checkboxes is not working
        if the checkboxes have variables which are not used in any method as arguments. So in order for this to work
        the variables of the checkboxes c3, c4 and c1 are used here.
        :param c3_dummy:
        :param c4_dummy:
        :param c1_dummy:
        """
        self.root.quit()


# Main Method
if __name__ == '__main__':
    # Todo: Delete this
    g = GUI()
