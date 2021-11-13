#By banksss33

import os
import sys
from cryptography.fernet import Fernet

class Gamesave():
    def __init__(self,username):
        self.username = username
    def create_save(self,password,game,win,lose,draw):
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
        with open(os.path.join(sys.path[0],self.username+".txt"),'wb') as fs: #create detail file
            detail = [self.username,password,game,win,lose,draw,winrate]
            for write_detail in detail:
                fs.write(fernet.encrypt(write_detail.encode())+b'\n')
                
    def load_save(self):
        with open(os.path.join(sys.path[0],self.username+".key"),'rb') as ls: #load key file
            key = ls.read()
            fernet = Fernet(key)
        with open(os.path.join(sys.path[0],self.username+".txt"),'rb') as ld: #load detail file
            saved_detail = []
            for n in range(7):
                detail = ld.readline()
                edetail = fernet.decrypt(detail).decode()
                saved_detail.append(edetail)
            return saved_detail

    def update_save(self,username,password,game,win,lose,draw):
        Game_update = Gamesave(username)
        Game_update.create_save(password,game,win,lose,draw)

#testing
Username = input("Username: ")
Password = input("Password: ")
game_name = "TICTACTOE"
game = Gamesave(Username)

try:
    stats = game.load_save()
    print(stats)
    if stats[0] == Username and stats[1] == Password:
        print("----------------------------------------")
        print("Hello welcome",Username+"!")
        detail_list = ["Game: ", "Win: ", "Lose: ", "Draw: ", "Winrate: "]
        for n in range(2,7):
            print(detail_list[n-2],stats[n])
        print("----------------------------------------")
    else:
        print("Wrong username or password!")
except:
    print("----------------------------------------")
    print("No save file found!")
    print("please create new savefile!")
    new_username = input("New Username: ")
    new_password = input("New Password: ")
    new_game = Gamesave(new_username)
    new_game.create_save(new_password,game_name,0,0,0)
    print("save file created!")
    print("----------------------------------------")
