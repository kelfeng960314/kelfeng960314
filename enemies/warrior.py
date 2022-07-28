# -*- coding: utf-8 -*-


import pygame
import os

from enemies.enemy import Boss, Boss_map2, Boss_map3


imgs = []
imgs_attack = []


for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str="0" + add_str
    imgs.append(
        pygame.transform.scale(
                            pygame.image.load(
                                            os.path.join("game_assets/enemies/4","0_boss_run_0" +add_str + ".png")
                                            ) 
                            ,(85,85)
                            )
        )


for x in range(20):
    add_str = str(x)
    if x < 10:
        add_str="0" + add_str
    imgs_attack.append(
        pygame.transform.scale(
                            pygame.image.load(
                                            os.path.join("game_assets/enemies/4","0_boss_attack_0" +add_str + ".png")
                                            ) 
                            ,(85,85)
                            )
        )






class Warrior(Boss):      

        
    def __init__(self):
         super().__init__()
         self.imgs[:] = imgs[:]
         self.imgs_attack[:] = imgs_attack[:]
         self.max_health =10
         self.health = self.max_health
         self.money = self.max_health
         self.name = "warrior"
         self.map = 1
         self.damage = 0.08
         self.range = 80




class Warrior_map2(Boss_map2):      

        
    def __init__(self):
         super().__init__()
         self.imgs[:] = imgs[:]
         self.imgs_attack[:] = imgs_attack[:]
         self.max_health =10
         self.health = self.max_health
         self.money = self.max_health
         self.name = "warrior"
         self.map = 2
         self.damage = 0.08
         self.range = 80
         
class Warrior_map3(Boss_map3):      

        
    def __init__(self):
         super().__init__()
         self.imgs[:] = imgs[:]
         self.imgs_attack[:] = imgs_attack[:]
         self.max_health =10
         self.health = self.max_health
         self.money = self.max_health
         self.name = "warrior"
         self.map = 3
         self.damage = 0.08
         self.range = 80         




