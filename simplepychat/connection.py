'''
Created on Jan 23, 2014

@author: keyvi_000
'''
import queue
import _thread as thread
import socket
import time


class connection():
    def __init__(self, address, port, dnick='Nonick1', dname='Bbob ford', incomingq=None, outgoingq=None):
        self.address = address
        self.port = port
        self.dnick = dnick
        self.dname = dname
        self.incomingq = incomingq
        self.outgoingq = outgoingq
       
    
    def readone(self):
        try:
            data = self.incomingq.get(False)
        except queue.Empty:
            data = ''
        return data
    
    def writeone(self, data):
        self.outgoingq.put(data)
    
    def startthread(self):
        thread.start_new_thread(dothread, (self.address, self.port, self.incomingq, self.outgoingq, self.dnick, self.dname))
    
    
    
    
def dothread(server, port, incomingq, outgoingq, dnick, dname): 
    Continue = True
    #connect to host, socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    incomingq.put("Connecting to " + server + " on port " + str(port))
    s.connect((server, int(port)))
    

    s.send(b'NICK ' + bytes(dnick, 'utf-8') + b'\r\n')
    s.send(b'USER ' + bytes(dnick, 'utf-8') + b' ' + bytes(dname, 'utf-8') + b' :pychat' + b'\r\n' )
    s.setblocking(False)#set indata to an empty binary string at start
    indata=b''
    while Continue:
        try:
            outdata = outgoingq.get(False)
        except queue.Empty:
            outdata = ''
        if outdata:
            
            outdata = outdata + '\r\n'
            outdata = bytes(outdata, 'utf-8')
            incomingq.put(str(outdata))
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
            #print (indata)
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
                        incomingq.put(str('PONG ' + i.split()[1] + '\r\n') )
                    #write line to output
                    incomingq.put(i)
                #clear input buffer
                indata = b''
            else:  #was not a complete command. Continue I/O loop until command is complete
                pass
       
        