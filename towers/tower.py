# -*- coding: utf-8 -*-

import pygame
from menu.menu import Menu_horizontial
import os

menu_bg = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","menu.png"))
                                 ,(120,55)
                                 )
upgrade_btn = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","upgrade.png"))
                                  ,(35,35)
                                  )

sell_btn = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","sell.png"))
                                  ,(30,30)
                                  )

star = pygame.transform.scale(
                    pygame.image.load (os.path.join("game_assets/menu","star.png" ))
                    ,(25,25)
                    )


class Tower:
    def __init__(self,x, y):
        self.x= x
        self.y=y
        self.width=0
        self.height=0
        self.sell_price = [0,0,0]
        self.price=[0,0,0]
        self.level=1
        self.selected = False
        self.tower_imgs = []
        self.damage = 1
        self.before_put = False
        
        self.menu = Menu_horizontial(self,self.x, self.y-70, menu_bg)

        self.exist = True

        
        
    
    def draw(self,win,move_x=None,move_y=None):

        
        # Tower picture if it is not moving
        img=self.tower_imgs[self.level-1]
        
        # before putting on the map, shows moving graphics
        if self.before_put == True:
            win.blit(img,(move_x-img.get_width()/2,move_y-img.get_height()/2) )

        else:
            self.draw_health_bar(win)
            win.blit(img,(self.x-img.get_width()/2,self.y-img.get_height()/2) )
        
       # Showes upgrade menu after being placed
        if self.selected and self.before_put == False:
            self.draw_radius(win)
            self.menu.draw(win)

    # Draw radius of effective area
    def draw_radius(self,win):
        if self.selected:
            # draw range circle
            surface = pygame.Surface((self.range*2,self.range*2) ,pygame.SRCALPHA , 32)   # 创建一个透明表面
            pygame.draw.circle(surface, (128,128,128,128), (self.range,self.range), self.range)  # 在透明表面上画圆
            win.blit(surface,(self.x-self.range,self.y-self.range))
        
    # Check if the tower is being clicked 
    def click(self,X,Y):

        if X <= self.x + self.width/2 and X >= self.x - self.width/2:
            if Y <= self.y + self.height/2 and Y >= self.y - self.height/2:
                return True
        return False

    # Tower upgrade
    def upgrade(self):
        if self.level <len(self.tower_imgs):
            self.level += 1
            self.damage +=1
            self.original_damage=self.damage
            self.health += 5
        
    # Tower cost
    def get_upgrade_cost(self):
        return self.price[self.level]
    
    # when tower get hit
    def get_hit(self,damage):
        self.health -=damage
        if self.health <=0:

            return True
        return False

   # draw the health bar of tower 
    def draw_health_bar(self,win):
        length = 50
        move_by = length /self.max_health
        health_bar = move_by * self.health
        
        pygame.draw.rect(win , (255,0,0),(self.x-25,self.y-42 , length , 7))
        pygame.draw.rect(win , (0,255,0),(self.x-25,self.y-42 , health_bar , 7))