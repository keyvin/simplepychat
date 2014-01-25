'''
Created on Jan 20, 2014

@author: keyvi_000
'''

#hello GIT

from tkinter import *

from pychat.connection import connection
from pychat.dataprocessing import ircprocessor

class pychatgui():
    def __init__(self):
        self.preferences = preferences()
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
        self.textproc = ircprocessor()
        self.tkframe.mainloop()
       
    def entryhandler(self, event):
        if self.connection:
            command = self.textproc.parseinput(self.tkentry.get())
            self.connection.writeone(command)
            self.tkentry.delete(0, END)
        
    def makemenu(self):
        
        self.menubar = Menu(self.tkframe)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Connect", command=self.connectmenu)
        filemenu.add_command(label="Quit", command=self.tkframe.quit)
        preferences = Menu(self.menubar, tearoff=0)
        preferences.add_command(label='Preferences', command=self.preferencemenu)
        self.menubar.add_cascade(label="File", menu=filemenu)
        self.menubar.add_cascade(label='Preferences', menu=preferences)

    def preferencemenu(self):
        self.preferences.dogui(self.tkframe)
        self.tkframe.wait_window(self.preferences.top)
        
        
    def connectmenu(self):
        connect = connectdialog(self.tkframe)
        self.tkframe.wait_window(connect.top)
        if connect.connected == True:
            self.connection = connection(connect.server, connect.port, self.preferences.nick, self.preferences.name)
            self.connection.startthread()
            self.tkframe.after(100,self.update)
        
    def update(self):
        data = self.connection.readone()
        while data != '':
            data = data.rstrip()
            if data:
                self.tktext.config(state=NORMAL)
                self.tktext.insert(END, data+'\n')
                self.tktext.yview(END)
                self.tktext.config(state=DISABLED)
        
            data = self.connection.readone()
        self.tkframe.after(100, self.update)

class preferences():
    def __init__(self):
        self.load()
    
    def dogui(self, parent):
        self.top = Toplevel(parent)
        Label(self.top, text="Nick").pack()
        self.nickentry = Entry(self.top)
        self.nickentry.insert(0, self.nick)
        self.nickentry.pack()
        Label(self.top, text='Name').pack()
        self.nameentry = Entry(self.top)
        self.nameentry.insert(0, self.name)
        self.nameentry.pack()
        Button(self.top, text="Save", command=self.savebutton).pack()
        
    def savebutton(self):
        self.nick = self.nickentry.get()
        self.name = self.nameentry.get()
        self.save()
        self.top.destroy()
    def save(self):
        file = open('chatpref.txt', 'w')
        file.write( self.nick + '\n')
        file.write(self.name + '\n')
        file.close()
    def load(self):
        try:
            file = open('chatpref.txt', 'r')
            self.nick = file.readline().rstrip()
            self.name = file.readline().rstrip()
            file.close()
        except FileNotFoundError:
            self.nick='Default096'
            self.name = "John Doe"
            
    
        
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


    