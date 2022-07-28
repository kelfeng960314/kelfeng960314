# -*- coding: utf-8 -*-

import pygame
from menu.menu import Menu_horizontial, Button
import os

pygame.init()
pygame.font.init()


levelend_table = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","levelend_table.png"))
                                 ,(300,375)
                                 )

button_close = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_close.png"))
                                 ,(80,80)
                                 )










button_close = Button(600-40-80, 130+375-100   , button_close, "button_close")

rank1_score = 200
rank1_name ="qwe"





 


title_menu_font = pygame.font.SysFont("name", 50)
text_title_menu = title_menu_font.render("TOP 10", 1, (255,255,255))





# create a scoreboard menu,which will let you to check the scoreboard and save your record

class Menu_scoreboard(Menu_horizontial):
    def __init__(self):
        self.width=300
        self.height=375
        self.top_left=(450-300/2,130)
        self.bg = levelend_table
        self.buttons = [button_close]
        self.rank_font= pygame.font.SysFont("name", 30) 
        self.text_rank = []          # a list store the top ten rank
        
    def draw(self, win):
        super().draw(win)

        win.blit(text_title_menu, (450-100,180)) 
        
        # draw the top ten rank
        for i in range(10):
            win.blit(self.text_rank[i], (450-100,220+i*25))
    
    # updata the rank when players save theirs
    def update(self):
        scoreboard = open('scoreboard.txt','r')
        c = scoreboard.readlines() 
        scoreboard.close()
        
        # rank the top ten rank
        for i in range(len(c) -1 ):
            for j in range(len(c) -i -1 ):
                if int(c[j][9:-1]) < int(c[j+1][9:-1]):
                    c[j] , c[j+1] = c [j+1], c[j]
        self.text_rank = []
        for i in range(10):
            self.text_rank.append(
                            self.rank_font.render( str(i+1)+" , " +c[i][0:8]+ " : " + str( c[i][9:-1] ).ljust(6)  ,
                                                1,(255,255,255) 
                                                )
                            )
        
        
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        