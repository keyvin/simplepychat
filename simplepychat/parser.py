'''
This class parses input, and calls functions as necessary. Might need to be split into multiple classes and
modules.
'''

import connection
import server
import window
import main




class parser():
    def __init__(self, incoming=None, outgoing=None, server=None):
        self.incoming = incoming
		self.outgoing = outgoing
		self.server = server
		
		return self
    def parseoutgoing(self, windowoforigin=None, intext=''):
		#needs to be changed to 
		#command
        if intext[0] == '/':
            if intext[0:5] == '/join':
                self.channel = intext[5:].lstrip()
                return 'JOIN ' + intext[5:].lstrip()
            if intext[0:5] == '/nick':
                return 'NICK ' + intext[5:].lstrip()
            if intext[0:4] == '/msg':
                txt = intext.split()
                return 'PRIVMSG ' + txt[1] + ' :' + ' '.join(txt[2:])
        else:
            return 'PRIVMSG ' + self.channel + ' :' + intext
        
        
    def parseincoming(self, windowlist='none'):
        #send messages to the appropriate windows
		#this function is called from server as a result 
		#of the after callback in the tk root.
		#it gets the windowlist from the server.getwindows() method.
		