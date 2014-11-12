'''This module contains the server class, 
which holds all windows, connections, and the parser for the server'''

class server():
	def __init__(self, tkroot=None, hostname='', tkroot = None,server=None ):
		#if hostname is empty, make an empty unconnected window, and set a flag so when connecting we do 
		#not reassign the window to a server that does not exist
		#if hostname is non empty, make a conn, add it to the conn list, create the queues, tie them to a parse
		#make a window, set an empty channel in that window
		# I need a data structure that ties windows to their channel names for the parser, so the 
		#parser knows where to send channel traffic, or what objects update room method I need to callable
		#to update the list of nicks in a channel.
		self.Parser = None
		self.Conn = None
		self.incoming = None
		self.outgoing = None
		self.windowlist = []
		self.tk = None
		return self
		
	def createconn(self, hostname):
		#creates a conn with the hostname. If a parser for this object does not yet exist, create that 
		#as well. 
		pass
		
	def createwindow(self):
		#creates a window, sets the channel to nothing. Maybe this should be done in parser. 
		#I can pass it to parser and it will share the reference, but that is pretty tight coupling
		pass
	def createparser(self):
		#if self.parser is None, make a parser, connect it to self.incoming and self.outgoing
		#it will then be connected. When parser is given input, it will call the addtext, adduser, deluser
		#methods of the window class to send the out. The window will send all input from the user to the parser
		#which will make the necessary callbacks in main, server, etc if necessary, send the data to the conn, etc
		pass
	def updatecallback(self):
		#check for input on the incoming queue, send it to parser which will update the windows as necessary
		pass
	def passwindow(self):
		#returns a window object to be added to another connection. This will preserve the contents of 
		#the window
		pass
	def changechannel(self, window=None):
		#this function changes the channel in a window. Just a matter of updating the window's channel
		#called back from parser. Easy
		pass
		