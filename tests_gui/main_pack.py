from tkinter import *

titles = ["Step 1: Workflows",
          "Step 2: Places",
          "Step 3: Transitions",
          "Step 4: Arcs",
          "Step 5: Create Locations",
          "Step 6: Assign Locations",
          "Step 7: Create Sensors",
          "Step 8: Assign Sensors",
          "Step 9: Set Simulation Options",
          "Step 10: Set Output Options",
          ]


class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Internet-of-Things Simulation Engine (IoTSE) ALPHA GUI")
        # root.iconbitmap('/path/to/ico/icon.ico')
        master.geometry("800x600")
        self.CurrentStep = ""
        self.CurrentWorkflow = ""
        self.current_frame_index = 1
        self.Frames = []
        self.Headline = None
        self.create_all_frames(master)
        # self.WorkflowList = None

    def create_all_frames(self, master):
        self.create_top_frame(master)
        self.create_frame_1(master)
        self.create_frame_2(master)
        self.create_frame_3(master)
        self.create_frame_4(master)
        self.create_frame_5(master)
        self.create_frame_6(master)
        self.create_frame_7(master)
        self.create_frame_8(master)
        self.create_frame_9(master)
        self.create_frame_10(master)
        self.create_bottom_frame(master)

    def create_top_frame(self, master):
        top_frame = Frame(master, width=800, height=50)
        label_1 = Label(top_frame, text="Step 1: Create Workflows")
        label_1.pack(side=LEFT)
        self.Headline = label_1
        label_2 = Label(top_frame, text="Current Workflow: <none>")
        label_2.pack(side=LEFT)
        top_frame.pack(side=TOP)

    def create_frame_1(self, master):
        f1 = Frame(master, width=800, height=500)

        l1_1 = Label(f1, text="* including options")
        l1_1.pack()
        l1_2 = Label(f1, text="* only Workflows, Sensors, Locations, Assignments")
        l1_2.pack()
        l1_3 = Label(f1, text="Workflows")
        l1_3.pack()

        btn_1_1 = Button(f1, width=20, text="Load Scenario...", command=self.btn_load_scenario)
        btn_1_1.pack()
        btn_1_2 = Button(f1, width=20, text="Add Scenario...", command=self.btn_add_scenario)
        btn_1_2.pack()
        btn_1_3 = Button(f1, width=20, text="Create Workflow...", command=self.btn_create_workflow)
        btn_1_3.pack()
        btn_1_4 = Button(f1, width=20, text="Edit Workflow...", command=self.btn_edit_workflow)
        btn_1_4.pack()
        btn_1_5 = Button(f1, width=20, text="Delete Workflow...", command=self.btn_delete_workflow)
        btn_1_5.pack()
        btn_1_6 = Button(f1, width=20, text="Set as active Workflow", command=self.btn_set_active_wf)
        btn_1_6.pack()
        btn_1_7 = Button(f1, width=20, text="Jump to Simulation", command=self.btn_jump_simulation)
        btn_1_7.pack()

        listbox = Listbox(f1, selectmode="browse")
        listbox.pack(side=LEFT)
        scrollbar = Scrollbar(f1)
        scrollbar.pack(side=LEFT, fill=BOTH)
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        # self.WorkflowList = listbox

        f1.pack()
        self.Frames.append(f1)

    def create_frame_2(self, master):
        f2 = Frame(master, width=800, height=500)
        label_f2 = Label(f2, text="Frame 2")
        label_f2.pack()
        f2.forget()
        self.Frames.append(f2)

    def create_frame_3(self, master):
        f3 = Frame(master, width=800, height=500)
        label_f3 = Label(f3, text="Frame 3")
        label_f3.pack()
        f3.forget()
        self.Frames.append(f3)

    def create_frame_4(self, master):
        f4 = Frame(master, width=800, height=500)
        f4.forget()
        self.Frames.append(f4)

    def create_frame_5(self, master):
        f5 = Frame(master, width=800, height=500)
        f5.forget()
        self.Frames.append(f5)

    def create_frame_6(self, master):
        f6 = Frame(master, width=800, height=500)
        f6.forget()
        self.Frames.append(f6)

    def create_frame_7(self, master):
        f7 = Frame(master, width=800, height=500)
        f7.forget()
        self.Frames.append(f7)

    def create_frame_8(self, master):
        f8 = Frame(master, width=800, height=500)
        f8.forget()
        self.Frames.append(f8)

    def create_frame_9(self, master):
        f9 = Frame(master, width=800, height=500)
        f9.forget()
        self.Frames.append(f9)

    def create_frame_10(self, master):
        f10 = Frame(master, width=800, height=500)
        f10.forget()
        self.Frames.append(f10)

    def create_bottom_frame(self, master):
        bottom_frame = Frame(master, width=800, height=50,)
        btn_prev = Button(bottom_frame, width=20, text="<- Previous", command=self.btn_previous_frame)
        btn_prev.pack(side=LEFT)
        btn_next = Button(bottom_frame, width=20, text="Next ->", command=self.btn_next_frame)
        btn_next.pack(side=LEFT)
        bottom_frame.pack(side=BOTTOM)

    def btn_previous_frame(self):
        if self.current_frame_index == 1:
            pass
        else:
            self.Frames[self.current_frame_index-1].forget()
            self.current_frame_index -= 1
            self.Frames[self.current_frame_index-1].pack()
            self.Headline.config(text=titles[self.current_frame_index-1])

    def btn_next_frame(self):
        if self.current_frame_index == 10:
            pass
        else:
            self.Frames[self.current_frame_index-1].forget()
            self.current_frame_index += 1
            self.Frames[self.current_frame_index-1].pack()
            self.Headline.config(text=titles[self.current_frame_index-1])

    def btn_load_scenario(self):
        # TODO
        pass

    def btn_add_scenario(self):
        # TODO
        pass

    def btn_create_workflow(self):
        # PopupCreateWorkflow(self.WorkflowList)
        # TODO
        pass

    def btn_edit_workflow(self):
        # TODO
        pass

    def btn_delete_workflow(self):
        # TODO
        pass

    def btn_set_active_wf(self):
        # TODO
        pass

    def btn_jump_simulation(self):
        # TODO
        pass

    # def add_to_workflows(self, a):
    #     self.WorkflowList.insert("end", a)
    #     self.CurrentWorkflow.config(text=a)


# class PopupCreateWorkflow:
#     def __init__(self, callback):
#         self.Gui = callback
#         self.Value = ""
#         popup = Tk()
#         popup.wm_title("!")
#         norm_font = ("Verdana", 10)
#         message_text = "Hallo, dies ist ein Popup"
#         label_x = Label(popup, text=message_text, font=norm_font)
#         label_x.pack(side="top", fill="x", pady=10)
#         e1 = Entry(popup)
#         e1.pack()
#         self.Value = e1
#         b1 = Button(popup, text="Cancel", command=popup.destroy)
#         b1.pack()
#         b2 = Button(popup, text="Save", command=self.save)
#         b2.pack()
#         popup.mainloop()
#
#     def save(self):
#         wf = self.Value.get()
#         self.Gui.insert("end", wf)


if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.mainloop()
