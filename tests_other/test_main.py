from tkinter import *
import tkinter.filedialog as fd
import tests_other.pnmlparser
import main_program.workflow_analyser

Workflows = []  # List of all loaded workflows
root = Tk()  # The gui

# Open files dialogue window and save all files references in variable
files = fd.askopenfilenames(parent=root, title='Choose a file')

for f in files:
    wf = tests_other.pnmlparser.parse_file(f)
    if main_program.workflow_analyser.analyse_workflow(wf):
        Workflows.append(wf)

for w in Workflows:
    for n in range(10):
        # w.run()
        w.run_repeatedly()
        # w.reset()
