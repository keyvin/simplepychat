"""This file is the main class for pychat. Functionality that I am adding is the ability to have more than
	one window open at a time, with connections to multiple channels """

import window
import connection
import server
from tkinter import *

#There should only be one control object ever created. I would make it a singleton but I do not know how
#in python

#serverlist data structure
class control():
	def __init__(self):
		#this function will do what is necessary to load preferences, create an empty server,
		#etc, etc
		self.serverlist = []
	#	self.s = server.server(self.tk, hostname='irc.synirc.org', nick='zobzan' )
		self.createtk()
		self.s = server.server(self.tk, hostname='irc.synirc.org', nick='zobzan' )
		
		
	def createserver(self, server=''):
		#create a server, if server is empty, init an unconnected window
		pass

	def destroyserver(self, server=''):
		#check if server is '' do nothing
		#check if server is last, exit
		#otherwise, delete reference to the server from the list
		pass
	def createtk(self):
		self.tk = Tk()
		
	def gettk(self):
		return self.tk
	def loadprofile(self):
		return self.tk

	def transferwindow(self, window=None):
		#callback function to transfer control of a window from one server to another
		pass
	
	def procincoming(self):
		print ("In callback\n")
		self.s.procincoming()
		print ("In callback\n")
		self.tk.after(100, self.procincoming )	
	
		


if __name__=='__main__':
	control = control()
	control.procincoming()
	control.tk.mainloop()
	
	