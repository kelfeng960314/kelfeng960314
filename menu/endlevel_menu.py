# -*- coding: utf-8 -*-

import pygame
from menu.menu import Menu_horizontial, Button
import os


levelend_table = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","levelend_table.png"))
                                 ,(300,375)
                                 )

winlogo = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","winlogo.png"))
                                 ,(150,60)
                                 )
failedlogo = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","failedlogo.png"))
                                 ,(150,60)
                                 )

button_play = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_play.png"))
                                 ,(150,150)
                                 )

button_restart = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_restart.png"))
                                 ,(80,80)
                                 )

button_close = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_close.png"))
                                 ,(80,80)
                                 )
button_right = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_right.png"))
                                 ,(80,80)
                                 )
button_scoreboard = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_empty.png"))
                                 ,(125,60)
                                 )


save_score = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","save_score.png"))
                                 ,(83,49)
                                 )




button_restart = Button(300+40, 130+375-100   , button_restart, "button_restart")
button_right = Button(300+40, 130+375-100   , button_right, "button_right")
button_close = Button(600-40-80, 130+375-100   , button_close, "button_close")
save_score = Button(450-83/2, 330   , save_score, "save_score")
button_scoreboard = Button(750, 500   , button_scoreboard, "button_scoreboard")



# create an menu which will show when player pass a level of game    
class Menu_endlevel_win(Menu_horizontial):
    def __init__(self):
        self.width=300
        self.height=375
        self.top_left=(450-300/2,130)
        self.bg = levelend_table
        self.logo = winlogo
        self.buttons = [button_right,button_close,save_score,button_scoreboard]        

    
    def draw(self, win):
        super().draw(win)
        win.blit(self.logo,(450-150/2 ,120))
        score_menu_font = pygame.font.SysFont("name", 25)
        text_score_menu = score_menu_font.render("scoreboard", 1, (255,255,255))
        win.blit(text_score_menu, (765,520))
        
# create an menu which will show when player failed a level of game        
class Menu_endlevel_failed(Menu_endlevel_win):
    def __init__(self):
        super().__init__()
        self.logo = failedlogo
        self.buttons = [button_restart,button_close,save_score,button_scoreboard]

        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        