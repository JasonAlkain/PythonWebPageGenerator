
from tkinter import *
import tkinter as tk

import main
import project_func


def load_gui(self):
    """
        Define the default tkinter widgets and their initial
        configuration and place them using the grid geometry.
        I prefer to use grid as it offers the best control
        for pacing the widgets, but is a little confusing at
        first, but that is what this demo is here for...
    """

    #################################
    # Label Setup
    #################################
    # Header Label
    self.lbl_h1 = Label(self.master, text='Header input:')
    self.lbl_h1["font"] = ('Arial', 16)
    self.lbl_h1["fg"] = 'whitesmoke'
    self.lbl_h1["bg"] = '#303030'
    # Paragraph Label
    self.lbl_p = Label(self.master, text='Paragraph input:')
    self.lbl_p["font"] = ('Arial', 16)
    self.lbl_p["fg"] = 'whitesmoke'
    self.lbl_p["bg"] = '#303030'
    # Notification
    self.lbl_display = Label(self.master, text='Notification Area')
    self.lbl_display["font"] = ('Arial', 16)
    self.lbl_display["bg"] = '#666'
    self.lbl_display["fg"] = 'whitesmoke'
    self.lbl_display["height"] = 4
    self.lbl_display["width"] = 20

    #################################
    # Entry Setup
    #################################
    # Header entry
    self.txt_h1 = Entry(self.master, text=self.header_html)
    self.txt_h1["font"] = ('Arial', 16)
    self.txt_h1["bg"] = 'whitesmoke'
    self.txt_h1["fg"] = 'black'
    # Paragraph entry
    self.txt_p = Entry(self.master, text=self.paragraph_html)
    self.txt_p["font"] = ('Arial', 16)
    self.txt_p["bg"] = 'whitesmoke'
    self.txt_p["fg"] = 'black'
    #################################
    # Button Setup
    #################################
    # Submit Button Setup
    self.btn_submit = Button(self.master)
    self.btn_submit["text"] = 'Submit'
    self.btn_submit["width"] = 10
    self.btn_submit["height"] = 2
    self.btn_submit["command"] = lambda: project_func.submit(self)
    self.btn_submit["bg"] = '#65FF80'
    # Open Button Setup
    self.btn_Open = Button(self.master)
    self.btn_Open["text"] = 'Open'
    self.btn_Open["width"] = 10
    self.btn_Open["height"] = 2
    self.btn_Open["command"] = lambda: project_func.openPage(self)
    self.btn_Open["bg"] = '#A0A0F0'
    # Close Button Setup
    self.btn_close = Button(self.master)
    self.btn_close["text"] = 'Close'
    self.btn_close["width"] = 10
    self.btn_close["height"] = 2
    self.btn_close["command"] = lambda: project_func.ask_quit(self)
    self.btn_close["bg"] = '#FF8090'

    #################################
    # label fields
    #################################
    self.lbl_h1.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))
    self.lbl_p.grid(row=1, column=0, padx=(20, 0), pady=(20, 0))
    self.lbl_display.grid(row=2, column=1, rowspan=3, columnspan=4,
                          padx=(20, 0), pady=(20, 0))
    #################################
    # text fields
    #################################
    self.txt_h1.grid(row=0, column=1, columnspan=4, padx=(20, 0), pady=(20, 0))
    self.txt_p.grid(row=1, column=1, columnspan=4, padx=(20, 0), pady=(20, 0))
    #################################
    # Button
    #################################
    self.btn_Open.grid(
        row=5, column=0, padx=(20, 0), pady=(20, 0), sticky=NW)
    self.btn_submit.grid(
        row=5, column=2, padx=(20, 0), pady=(20, 0), sticky=NE)
    self.btn_close.grid(
        row=5, column=4, padx=(20, 0), pady=(20, 0), sticky=NE)


if __name__ == "__main__":
    pass
