#
import os
import time
import tkinter as tk
from tkinter import *
import webbrowser

#
import project_gui
import main


#
def center_window(self, w, h):  # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


#
def submit(self):
    _h1s = self.header_html.get()
    _ps = self.paragraph_html.get()
    self.lbl_display.config(text='Changes made!\n{}\n{}'.format(_h1s, _ps))
    htmlDoc = htmlSetup(self)
    writeData('index.html', '{}'.format(htmlDoc), 'w')
    #self.lbl_display.config(text='')


#
def openPage(self):
    self.lbl_display.config(text='Opening web page...')
    webbrowser.open_new_tab('index.html')


#
def cancel(self):
    self.master.destroy()


# catch if the user's clicks on the windows upper-right 'X' to ensure they want to close
def ask_quit(self):
    if self.messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # This closes app
        self.master.destroy()
        os._exit(0)


def writeData(fileName='', data='', openMode='a'):
    data = data  # 'Hello, world'
    with open(fileName, openMode) as f:
        data = f.write(data)
        f.close()


def openFile(fileName=''):
    data = ''
    if fileName != '':
        with open(fileName, 'r') as f:
            data = f.read()
            f.close()
    return data


def testHtml(self):
    _hs = htmlSetup(self)
    print(_hs)


def body_html(self):
    _h1s = '\n\t\t<h1>{}</h1>'.format(self.header_html.get())
    _ps = '\n\t\t<p>{}</p>'.format(self.paragraph_html.get())
    section = '<div>{}{}\n\t</div>'.format(_h1s, _ps)
    return section


# Returns a template html document with the inner html
def htmlSetup(self):
    docType = '<!DOCTYPE html>'
    metaTags = ['<meta charset="UTF-8">', '<meta http-equiv="X-UA-Compatible" content="IE=edge">',
                '<meta name="viewport" content="width=device-width, initial-scale=1.0">']
    titleTag = '<title>PWPG</title>'
    headTag = '<head>\n\t{}\n\t{}\n\t{}\n\t{}\n</head>'.format(
        metaTags[0], metaTags[1], metaTags[2], titleTag)
    bodyTag = '<body>\n\t{}\n</body>'.format(body_html(self))
    htmlTag = '<html lang="en">\n{}\n{}\n</html>'.format(headTag, bodyTag)
    return '{}\n{}'.format(docType, htmlTag)


if __name__ == "__main__":
    pass
