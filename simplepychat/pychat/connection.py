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
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rqueue.put("Connecting to " + server + " on port " + port)
    s.connect((server, int(port)))
    s.setblocking(False)
    while Continue:
        try:
            data = wqueue.get(False)
        except queue.Empty:
            data = ''
        if data:
            
            data = data + '\r\n'
            data = bytes(data, 'utf-8')
            rqueue.put(str(data))
            s.send(data)
            print(data)
        try:
            data = s.recv(4096)
            print (data)
            if data==b'':
                break
            rqueue.put(data.decode(errors='ignore'))
            if data[0:4] == b'PING':
                b = s.send(b'PONG ' + data.split()[1] + b'\r\n' )
                print (b)
                rqueue.put(str(b'PONG ' + data.split()[1] + b'\r\n') )
        except socket.error:
            pass
        