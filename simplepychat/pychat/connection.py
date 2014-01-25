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
    #connect to host, socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rqueue.put("Connecting to " + server + " on port " + port)
    s.connect((server, int(port)))
    s.setblocking(False)
    #set indata to an empty binary string at start
    indata=b''
    while Continue:
        try:
            outdata = wqueue.get(False)
        except queue.Empty:
            outdata = ''
        if outdata:
            
            outdata = outdata + '\r\n'
            outdata = bytes(outdata, 'utf-8')
            rqueue.put(str(outdata))
            s.send(outdata)
            print(outdata)
        #set received flag false so we know we haven't received anything this loop
        received = False     
        #try for non blocking I/O
        try:
            #get all available data, reading 2048 bytes at a time
            while True:  
                d = s.recv(12000)
                received = True
                indata = indata + d #append to in data
        except socket.error:
            pass
        #if we received something in the try catch
        if received:
            print (indata)
            #if it is an empty string then socket is dead, break out of loop, ending thread
            if indata==b'':
                break
            #check to see if the command is complete - this is signified by ending with crlf
            if indata[-2:] == b'\r\n':
                #convert to string so split will work, split input into individual commands
                for i in indata.decode(errors='ignore').split('\r\n'):
                    #if it is a ping, send a pong
                    if i[0:4] == 'PING':
                        b = s.send(b'PONG ' + bytes(i.split()[1], encoding='utf-8') + b'\r\n' )
                        print (b)
                        rqueue.put(str('PONG ' + i.split()[1] + '\r\n') )
                    #write line to output
                    rqueue.put(i)
                #clear input buffer
                indata = b''
            else:  #was not a complete command. Continue I/O loop until command is complete
                pass
       
        