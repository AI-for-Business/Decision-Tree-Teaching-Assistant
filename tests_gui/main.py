from tkinter import *


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
        self.create_all_frames(master)

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

    @staticmethod
    def create_top_frame(master):
        top_frame = Frame(master, width=800, height=50)
        label_1 = Label(top_frame, text="Step 1: Create Workflows")
        label_1.grid(row=0, column=0, padx='5', pady='5')
        label_2 = Label(top_frame, text="Current Workflow: <none>")
        label_2.grid(row=0, column=1, padx='5', pady='5')
        top_frame.grid()

    def create_frame_1(self, master):
        f1 = Frame(master, width=800, height=500)
        label_f1 = Label(f1, text="Frame 1")
        label_f1.grid(row=0, column=0, padx='5', pady='5')
        f1.grid()
        self.Frames.append(f1)

    def create_frame_2(self, master):
        f2 = Frame(master, width=800, height=500)
        label_f2 = Label(f2, text="Frame 2")
        label_f2.grid(row=0, column=0, padx='5', pady='5')
        f2.grid()
        f2.grid_remove()
        self.Frames.append(f2)

    def create_frame_3(self, master):
        f3 = Frame(master, width=800, height=500)
        label_f3 = Label(f3, text="Frame 3")
        label_f3.grid(row=0, column=0, padx='5', pady='5')
        # f3.grid()
        f3.grid_remove()
        self.Frames.append(f3)

    def create_frame_4(self, master):
        f4 = Frame(master, width=800, height=500)
        # f4.grid()
        f4.grid_remove()
        self.Frames.append(f4)

    def create_frame_5(self, master):
        f5 = Frame(master, width=800, height=500)
        # f5.grid()
        f5.grid_remove()
        self.Frames.append(f5)

    def create_frame_6(self, master):
        f6 = Frame(master, width=800, height=500)
        # f6.grid()
        f6.grid_remove()
        self.Frames.append(f6)

    def create_frame_7(self, master):
        f7 = Frame(master, width=800, height=500)
        # f7.grid()
        f7.grid_remove()
        self.Frames.append(f7)

    def create_frame_8(self, master):
        f8 = Frame(master, width=800, height=500)
        # f8.grid()
        f8.grid_remove()
        self.Frames.append(f8)

    def create_frame_9(self, master):
        f9 = Frame(master, width=800, height=500)
        # f9.grid()
        f9.grid_remove()
        self.Frames.append(f9)

    def create_frame_10(self, master):
        f10 = Frame(master, width=800, height=500)
        # f10.grid()
        f10.grid_remove()
        self.Frames.append(f10)

    def create_bottom_frame(self, master):
        bottom_frame = Frame(master, width=800, height=50,)
        btn_prev = Button(bottom_frame, width=20, text="Previous", command=self.btn_previous_frame)
        btn_prev.grid(row=0, column=0, padx='5', pady='5')
        btn_next = Button(bottom_frame, width=20, text="Next", command=self.btn_next_frame)
        btn_next.grid(row=0, column=4, padx='5', pady='5')
        bottom_frame.grid()

    def btn_previous_frame(self):
        if self.current_frame_index == 1:
            pass
        else:
            self.Frames[self.current_frame_index-1].grid_remove()
            self.current_frame_index -= 1
            self.Frames[self.current_frame_index-1].grid()

    def btn_next_frame(self):
        if self.current_frame_index == 10:
            pass
        else:
            self.Frames[self.current_frame_index-1].grid_remove()
            self.current_frame_index += 1
            self.Frames[self.current_frame_index-1].grid()


if __name__ == "__main__":
    root = Tk()
    gui = GUI(root)
    root.mainloop()
