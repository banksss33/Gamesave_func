#banksss33

import os
import sys
from cryptography.fernet import Fernet

class Gamesave():
    def __init__(self,username):
        self.username = username
    def create_save(self,password,game,win,lose,draw): #create detail file
        key = Fernet.generate_key()
        fernet = Fernet(key)
        All_game = win+lose+draw    
        if All_game == 0:
            winrate = 0
        else:
            winrate = win/All_game*100
        winrate = str(winrate)
        win = str(win)
        lose = str(lose)
        draw = str(draw)
        with open(os.path.join(sys.path[0],self.username+".key"),'wb') as fk: #create key file
            fk.write(key)
        with open(os.path.join(sys.path[0],self.username+".csv"),'wb') as fs: #create detail file
            fs.write(fernet.encrypt(password.encode())+b'\n')
            fs.write(fernet.encrypt(game.encode())+b'\n')
            fs.write(fernet.encrypt(win.encode())+b'\n')
            fs.write(fernet.encrypt(lose.encode())+b'\n')
            fs.write(fernet.encrypt(draw.encode())+b'\n')
            fs.write(fernet.encrypt(winrate.encode())+b'\n')

    def load_save(self): #load detail file
        with open(os.path.join(sys.path[0],self.username+".key"),'rb') as ls: #load key file
            key = ls.read()
            fernet = Fernet(key)
        with open(os.path.join(sys.path[0],self.username+".csv"),'rb') as ld: #load detail file
            saved_detail = []
            for n in range(6):
                detail = ld.readline()
                edetail = fernet.decrypt(detail).decode()
                saved_detail.append(edetail)
            return saved_detail

    def update_save(self,username,password,game,win,lose,draw): #update detail
        Game_update = Gamesave(username)
        Game_update.create_save(password,game,win,lose,draw)