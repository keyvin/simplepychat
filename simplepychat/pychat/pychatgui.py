'''
Created on Jan 20, 2014

@author: keyvi_000
'''

#hello GIT

from tkinter import *

from connection import *

class pychatgui():
    def __init__(self):
        
        #top level widget
        self.tkframe = Tk()
        #for the scroll bar, entry, and text widget
        self.rightframe = Frame(self.tkframe)
        self.rightframe.pack(side=RIGHT, fill=BOTH, expand=YES)
        #for the list  box widget
        self.leftframe = Frame(self.tkframe)
        self.leftframe.pack(side=LEFT, fill=Y)
        self.tkentry = Entry(self.rightframe)
        self.tktext = Text(self.rightframe)
        self.tklistbox = Listbox(self.leftframe)        
        self.tklistbox.pack(fill=Y, expand=YES)
        self.tktext.pack(fill=BOTH, expand=YES)
        self.tkentry.pack(fill=X, expand=NO)
        self.tkentry.bind('<Return>', self.entryhandler)
        self.makemenu()
        self.tkframe.config(menu=self.menubar)
        self.tktext.config(state=DISABLED)
        self.connection = ''
        self.tkframe.mainloop()
       
    def entryhandler(self, event):
        if self.connection:
            self.connection.writeone(self.tkentry.get())
            self.tkentry.delete(0, END)
        
    def makemenu(self):
        
        self.menubar = Menu(self.tkframe)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Connect", command=self.connectmenu)
        filemenu.add_command(label="Quit", command=self.tkframe.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

    def connectmenu(self):
        connect = connectdialog(self.tkframe)
        self.tkframe.wait_window(connect.top)
        if connect.connected == True:
            self.connection = connection(connect.server, connect.port)
            self.connection.startthread()
            self.tkframe.after(100,self.update)
        
    def update(self):
        data = self.connection.readone()
        if data:
            self.tktext.config(state=NORMAL)
            self.tktext.insert(END, data+'\n')
            self.tktext.yview(END)
            self.tktext.config(state=DISABLED)
        self.tkframe.after(100, self.update)
        
class connectdialog():
    def __init__(self, parent):
        self.connected = False
        self.top = Toplevel(parent)
        
        Label(self.top, text="Server").pack()
        self.sentry = Entry(self.top)
        self.sentry.pack()
        Label(self.top, text="Port").pack()
        self.pentry = Entry(self.top)
        self.pentry.pack()
        Button(self.top, text="Connect", command=self.connectbutton).pack()
        Button(self.top, text="Cancel", command=self.top.destroy).pack()
    def connectbutton(self):
        self.connected = True
        self.server = self.pentry.get()
        self.port = self.sentry.get()
        self.top.destroy()

n = pychatgui()


    