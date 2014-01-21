'''
Created on Jan 20, 2014

@author: keyvi_000
'''

#hello GIT

from tkinter import *;

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
        self.tkframe.mainloop()
        
    def entryhandler(self, event):
        self.tktext.config(state=NORMAL)
        self.tktext.insert(END, self.tkentry.get()+'\n')
        self.tktext.yview(END)
        self.tktext.config(state=DISABLED)
        self.tkentry.delete(0, END)
        
    def makemenu(self):
        
        self.menubar = Menu(self.tkframe)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Connect", command=self.connectmenu)
        filemenu.add_command(label="Quit", command=self.tkframe.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

    def connectmenu(self):
        connection = connectdialog(self.tkframe)
        self.tkframe.wait_window(connection.top)
        if connection.connected == True:
            pass

        
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
        self.server = self.sentry.get()
        self.port = self.pentry.get()
        self.top.destroy()

n = pychatgui()


    