# -*- coding: utf-8 -*-


import pygame
import os

from enemies.enemy import Enemy,Enemy_map2,Enemy_map3




imgs = []
    
for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str="0" + add_str
    imgs.append(
        pygame.transform.scale(
                            pygame.image.load(
                                            os.path.join("game_assets/enemies/2","2_enemies_1_run_0" +add_str + ".png")
                                            ) 
                            ,(64,64)
                            )
        )

class Wizard(Enemy):      
            
        
    def __init__(self):
         super().__init__()
         self.imgs[:] = imgs[:]
         self.max_health =6
         self.health = self.max_health
         self.money = self.max_health 
         self.name = "wizard"
         self.map = 1 
         
         
class Wizard_map2(Enemy_map2):      
    
    def __init__(self):
         super().__init__()
         self.imgs[:] = imgs[:]
         self.max_health =6
         self.health = self.max_health
         self.money = self.max_health 
         self.name = "wizard" 
         self.map = 2
        
        
class Wizard_map3(Enemy_map3):      
    
    def __init__(self):
         super().__init__()
         self.imgs[:] = imgs[:]
         self.max_health =6
         self.health = self.max_health
         self.money = self.max_health 
         self.name = "wizard"  
         self.map = 3           
    