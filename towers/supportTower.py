# -*- coding: utf-8 -*-

import pygame
import os
import math
from menu.menu import Menu_horizontial
from towers.tower import Tower

# from menu.menu import Menu


menu_bg = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","menu.png"))
                                 ,(120,55)
                                 )
upgrade_btn = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","upgrade.png"))
                                 ,(60,60)
                                 )
range_imgs=[]
damage_imgs=[]

for x in range(2):
    add_str = str(x)
    range_imgs.append(
                pygame.transform.scale(
                        pygame.image.load(
                                        os.path.join("game_assets/support_towers", add_str + ".png")
                                        ) 
                ,(64,64)
                )
                            
        )

for x in range(2):
    add_str = str(x+2)
    damage_imgs.append(
                pygame.transform.scale(
                        pygame.image.load(
                                        os.path.join("game_assets/support_towers", add_str + ".png")
                                        ) 
                ,(64,64)
                )
                            
        )




# create the class of a range tower, which will increase the attack range of attack towers which is in range
class RangeTower(Tower):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.range = 150
        self.tower_imgs=range_imgs[:]
        self.effect = [0.3,0.6]
        self.height=self.tower_imgs[self.level-1].get_height()
        self.width=self.tower_imgs[self.level-1].get_width()

        self.buy_price = 300
        self.max_health=10
        self.health = self.max_health
        self.type = "support_tower"
    
        
    def draw(self,win,move_x=None,move_y=None):
        
        super().draw(win,move_x,move_y)
        # super().draw_radius(win)
        
        
    # increase the attack range of attack towers which is in range
    def support(self,towers):
        effected=[]
        for tower in towers:
            x = tower.x
            y = tower.y
            
            dis = math.sqrt( (self.x-x)**2 + (self.y-y)**2 )
            if dis<=self.range:
                effected.append(tower)
        for tower in effected:
            tower.range = tower.original_range + tower.original_range*self.effect[self.level-1]

 
            
# create the class of a damage tower, which will increase the damage of attack towers which is in range    
class DamageTower(RangeTower):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.range = 150
        self.tower_imgs=damage_imgs[:]
        self.max_health=10
        self.health = self.max_health
        
    # increase the damage of attack towers which is in range    
    def support(self,towers):
        effected=[]
        for tower in towers:
            x = tower.x
            y = tower.y
            
            dis = math.sqrt( (self.x-x)**2 + (self.y-y)**2 )
            if dis<=self.range:
                effected.append(tower)
        for tower in effected:
            tower.damage = tower.original_damage + tower.original_damage*self.effect[self.level-1]