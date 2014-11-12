"""This file is the main class for pychat. Functionality that I am adding is the ability to have more than
	one window open at a time, with connections to multiple channels """

import pychatgui
import connection

#There should only be one control object ever created. I would make it a singleton but I do not know how
#in python
class control():
	def __init__(self):
		#this function will do what is necessary to load preferences, create an empty server,
		#etc, etc
		self.serverlist = []
		return self
		
	def createserver(self, Server=''):
		#create a server, if server is empty, init an unconnected window
		pass
	def destroyserver(self, Server=''):
		#check if server is '' do nothing
		#check if server is last, exit
		#otherwise, delete reference to the server from the list
		pass
	def createtk(self):
		#creates the root tk 
		pass
	def loadprofile(self):
		#loads profile from db or text file
		pass
	def transferwindow(self, window=None)
		#callback function to transfer control of a window from one server to another
		pass
	def procincoming(self)
		
		pass
		


if __name__=='__main__':
	#create initial window
	
	