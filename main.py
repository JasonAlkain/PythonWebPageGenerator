import tkinter as tk
from tkinter import *
from tkinter import messagebox

import project_gui
import project_func


class Application(Frame):
    def __init__(self, master=None):
        #################################
        # Super init()
        #################################
        super().__init__(master)
        #################################
        # Master setup
        #################################
        self.master = master
        self.master.title('Learning TKinter!')
        self.master.resizable(width=False, height=False)
        self.master.geometry('{}x{}'.format(530, 320))
        self.master.config(bg='#303030')
        self.messagebox = messagebox
        self.master.protocol("WM_DELETE_WINDOW",
                             lambda: project_func.ask_quit(self))

        #################################
        # String Variable Setup
        #################################
        self.header_html = StringVar()
        self.paragraph_html = StringVar()
        self.htmlFull = StringVar()
        project_gui.load_gui(self)


if __name__ == '__main__':
    root = Tk()
    app = Application(root)

    app.mainloop()
