'''
Created on Jan 25, 2014

@author: keyvi_000
'''


class ircprocessor():
    def __init__(self):
        self.channel = '#none'
        pass
    def parseinput(self, intext):
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
        
        
    def parseoutput(self, outtext):
        pass