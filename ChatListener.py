global user
global oauth
import socket # connect to twitch
Running = True #im getting better at using less global varialbes, I still need this one tho
sock = socket.socket() #and this one
import time
import colorama
from multiprocessing import Process
import os
from colorama import Fore, Style
from colorama import init as colorInit
from names import * # your twitch login
time.sleep(0.2)

colorInit(convert=True)

class Chat():
    def __init__(self, channel):
        self.channel = channel
        try:
            self.channel = self.channel.lower()
        except:
            pass
            
            
    def connectToChat(self): # Connects to the chat
        sock.connect(('irc.chat.twitch.tv', 6667))
        time.sleep(0.1)
        sock.send(f'PASS {oauth}\n'.encode('utf-8'))
        time.sleep(0.1)
        sock.send(f'NICK {user}\n'.encode('utf-8'))
        time.sleep(0.1)
        sock.send(f'JOIN #{self.channel}\n'.encode('utf-8'))
        resp = sock.recv(2048).decode('utf-8')
        time.sleep(0.1)
    
    def call(self):
        while Running == True:
            resp = sock.recv(2048).decode('utf-8')
            time.sleep(0.1)
            try:
                income = resp.split(f'PRIVMSG #{self.channel} :', 1)
                message = income[1]
                user1 = income[0]
                user1 = user1.split(f':', 1)
                user2 = user1[1]
                user2 = user2.split(f'!', 1)
                username = user2[0]
                print(Fore.RED + Style.BRIGHT + self.channel + ' ' + Style.RESET_ALL + Fore.CYAN + username +': ' + Fore.WHITE + message + Style.RESET_ALL)
            except:
                pass
            if "PING :tmi.twitch.tv" in resp:
                sock.send(f'PONG :tmi.twitch.tv\n'.encode("utf-8"))
            elif (":" + user +".tmi.twitch.tv 366 " + user + " #" + self.channel + " :End of /NAMES list") in resp:
                print('Connected to #' + self.channel)
            else:
                pass
    
    def initialize(self):
        self.connectToChat()
        self.call()


