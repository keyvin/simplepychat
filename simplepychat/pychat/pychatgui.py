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
        self.menubar = Menu(self.tkframe)
        self.menubar.add_command(label="Connect", command=self.tkframe.quit )
        self.tklistbox.pack(fill=Y, expand=YES)
        self.tktext.pack(fill=BOTH, expand=YES)
        self.tkentry.pack(fill=X, expand=NO)
        self.tkentry.bind('<Return>', self.entryhandler)
        self.tkframe.config(menu=self.menubar)
        self.tkframe.mainloop()
        
    def entryhandler(self, event):
        self.tktext.insert(END, self.tkentry.get()+'\n')
        self.tktext.yview(END)
        self.tkentry.delete(0, END)

n = pychatgui()
