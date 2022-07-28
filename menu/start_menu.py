# -*- coding: utf-8 -*-

import pygame
from menu.menu import Menu_horizontial, Button
import os


start_bg = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","start_bg.png"))
                                 ,(900,600)
                                 )

logo = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","logo.png"))
                                 ,(450,150)
                                 )

button_play = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_play.png"))
                                 ,(150,150)
                                 )
# creata a menu start class,which is the start page
class Menu_Start(Menu_horizontial):
    def __init__(self):
        self.top_left=(0,0)
        self.bg = start_bg
        self.buttons=[]
        self.logo=logo
        self.buttons=[Button(450-150/2, 300, button_play, "button_play")]
    
    def draw(self, win):
        super().draw(win)
        win.blit(self.logo,(450-450/2,150))
        