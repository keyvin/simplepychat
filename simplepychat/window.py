'''
This class sets up windows. I need to split out the other dialogs. 
I need to add callbacks for parser to tell the windows to update. 
'''

#hello GIT

from tkinter import *

import connection
import parser
import server
import connection


class window():
    def __init__(self, server, tkroot, channel='', parser=None):
        #connects window to parent, gets tk object, uses it as root, but as a seperate window
		#that is non modal
		
        self.preferences = preferences()
        #top level widget
        self.tkframe = tkroot
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
        self.textproc = parser
        self.channel = channel
        self.parser = parser
        
 
    
    def entryhandler(self, event):
        
            self.parser.parseoutgoing(self, intext=self.tkentry.get())
            
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
            #self.connection.startthread()
           # self.tkframe.after(100,self.update)
    def checklines(self):
        #This function will check the number of lines compared to the global preferences and delete them as necessary. I need to add scrollback to the control as well.
        pass

    #This function will add nicks to the nick list. I need to make the nick list scrollable as well. 
    def addnicks(self, nicks=[]):
        pass

    #deletes nicks from the nick list. To do a name change, delete then add. 
    def delnicks(self, nicks=[]):
        pass
    
    #This function writes to the screen with no options     
    def writetext(self, data=''):
        self.tktext.config(state=NORMAL)
        self.tktext.insert(END, data+'\n')
        self.tktext.yview(END)
        self.tktext.config(state=DISABLED)

    #write chat message puts chat text with colors nicely on the screen
    def writemessage(nick='', message=''):
        pass

    #emotes
    def writeemote(nick='', emote=''):
        pass
    #joins, quits, etc.
    def writeservermessages(type='none', message=''):
        pass

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




    
