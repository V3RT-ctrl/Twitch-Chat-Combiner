from ChatListener import *

def connectMore():
    personname = input()
    object = Chat(personname)
    p = Process(target = object.initialize)
    p.start()
    
    
if __name__ == '__main__':
    sock.close()
    Running = True
    while Running == True:
        connectMore()