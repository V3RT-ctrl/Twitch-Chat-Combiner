from ChatListener import *

personIn = []
def connectMore():
    personname = input()
    if personname not in personIn:
        personIn.append(personname)
        object = Chat(personname)
        p = Process(target = object.initialize)
        try:
            p.start()
        except:
            print("Sometimes sockets is cringe. It's nothing that's your fault, it's just that python fucked up.")
            personIn.remove(personname)
    else:
        print('You are already connected to their chat!')
    

if __name__ == '__main__':
    Running = True
    while Running == True:
        connectMore()