# -*- coding: utf-8 -*-


import pygame
from menu.menu import Menu_vertical
import os

menu_bg = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","menu_vertical.png"))
                                 ,(70,320)
                                 )
#  create a purchase menu class, which is on the right of the screen
class Purchase_Menu:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.level=1
        self.menu= Menu_vertical(self,self.x, self.y, menu_bg) 
        
    
    def draw(self,win):
        self.menu.draw(win)
        