'''
This class parses input, and calls functions as necessary. Might need to be split into multiple classes and
modules.
'''

import connection
import server
import window
import main




class parser():
    def __init__(self, server, conn=None, nick='user5000'):
        self.server = server
        self.conn = conn
        self.nick = nick
		
        
    def parseoutgoing(self, win, intext=''):
		#needs to be changed to 
		#command
        #needs to call the window update methods
        if intext == '':
            return
        if intext[0] == '/':
            if intext[0:5] == '/join':
                self.channel = intext[5:].lstrip()
                com = 'JOIN ' + intext[5:].lstrip()
            if intext[0:5] == '/nick':
                com = 'NICK ' + intext[5:].lstrip()
            if intext[0:4] == '/msg':
                txt = intext.split()
                com = 'PRIVMSG ' + txt[1] + ' :' + ' '.join(txt[2:])
        else:
            com = 'PRIVMSG ' + self.channel + ' :' + intext
        
        self.conn.writeone(com)
        print (com)
    def ismessage(self, data):
        return True
    def changenick(self, newnick=''):
        self.nick=newnick
    def haschannel(self, data = ''):
        #does this data contain a channel?
        #we will just stub it for now
        return True
    def parsechannel(self, data=''):
        #this should parse out a channel, we will just use yospos for now
        return 'yospos'

    def procupdate(self):
        #no connection (yet)
        print ("in callback")
        if self.conn==None:
            return 
        data = self.conn.readone()
        winlist = self.server.getwinlist()
        while data != '':
            data = data.rstrip()
            #need to do some parsing here to get the channel
            if data=='':
                continue
            #if it isn't a message from the server we need to update the window
            if self.haschannel(data):
                if self.ismessage(data):
                    for win in winlist:
                        if win.channel == self.parsechannel(data) or win.channel=='':
                            win.writetext(data)   
        
            data = self.conn.readone()
        #this needs to go in the main to update the tkinter
        #self.tkframe.after(100, self.update)