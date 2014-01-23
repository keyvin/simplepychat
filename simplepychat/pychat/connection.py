'''
Created on Jan 23, 2014

@author: keyvi_000
'''
import queue
import _thread as thread
import socket

class connection():
    def __init__(self, port, address):
        self.address = address
        self.port = port
        self.readq = queue.Queue()
        self.writeq = queue.Queue()
    
    def readone(self):
        try:
            data = self.readq.get(False)
        except queue.Empty:
            data = ''
        return data
    
    def writeone(self, data):
        self.writeq.put(data)
    
    def startthread(self):
        thread.start_new_thread(dothread, (self.address, self.port, self.readq, self.writeq))
    
    
    
    
def dothread(server, port, rqueue, wqueue): 
    Continue = True
    while Continue:
        try:
            data = wqueue.get(False)
        except queue.Empty:
            data = ''
        if data:
            print(data)
            rqueue.put(data)