# -*- coding: utf-8 -*-


import pygame
import os
import math

from towers.tower import Tower



pygame.mixer.init()

# set different sound when enemy was defeated
tower_sound1=pygame.mixer.Sound("./game_assets/music/stone.mp3")
tower_sound2=pygame.mixer.Sound("./game_assets/music/fireball.mp3")            
    
# set volumn
tower_sound1.set_volume(0.5)
tower_sound2.set_volume(0.5)






menu_bg = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","menu.png"))
                                 ,(120,55)
                                 )
upgrade_btn = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","upgrade.png"))
                                 ,(60,60)
                                 )




tower1_imgs = []
shooter1_imgs=[]
stone1_imgs =[]


    
for x in range(3):
    add_str = str(x)
    tower1_imgs.append(
                pygame.transform.scale(
                        pygame.image.load(
                                        os.path.join("game_assets/stone_towers/stonetower1/foundation", add_str + ".png")
                                        ) 
                ,(64,64)
                )
                            
        )


for x in range(6):
    add_str = str(x)
    shooter1_imgs.append(
                pygame.transform.scale(
                        pygame.image.load(
                                        os.path.join("game_assets/stone_towers/stonetower1/shooter", add_str + ".png")
                                        ) 
                ,(64,14)
                )
                            
        )
    
for x in range(1):
    add_str = str(x)
    stone1_imgs.append(
                pygame.transform.scale(
                        pygame.image.load(
                                        os.path.join("game_assets/stone_towers/stonetower1/stone", add_str + ".png")
                                        ) 
                ,(15,15)
                )
                            
        )    







class StoneTower1(Tower):
    def __init__(self,x,y):
        super().__init__(x, y)
        # img of tower
        self.tower_imgs=tower1_imgs[:]   
        self.shooter_imgs=shooter1_imgs[:]
        self.stone_imgs =stone1_imgs[:]
        self.stone_count = 0
        self.move_distance = 0       # distance of shooter go up
        self.range = 110             # attack range
        self.original_range = 100
        self.inrange = False         # if enemy in range

        self.attack_F = 1             # attack frequency
        self.attack_F_original = 1            
        self.damage = 1               # the damage this tower will create
        self.original_damage = 1
        self.height=self.tower_imgs[self.level-1].get_height()
        self.width=self.tower_imgs[self.level-1].get_width()
        self.buy_price = 500         # the money to buy this tower
        self.pause = False
        self.music = True
        self.name = "StoneTower1"
        self.max_health=10           # the max health
        self.health = self.max_health
        self.type = "attack_tower"

        
        
    # draw this tower
    def draw(self,win,move_x=None,move_y=None):
        
        # if this tower is not be put, draw it through dynamic coordinate
        if self.before_put == True:
            super().draw(win,move_x,move_y)
        else:
            shooter_imgs_back=self.shooter_imgs[self.level-1]            
            shooter_imgs_front=self.shooter_imgs[self.level+2]           
            
            
            height_diff=shooter_imgs_back.get_height()-3    
            height_diff2 = 7.5                              
            

            # through every loop of game function self.move_distance += self.attack_F，to achieve the animation effect
             
            if self.move_distance < 50 :
                win.blit(shooter_imgs_back,(self.x-shooter_imgs_back.get_width()/2,self.y-shooter_imgs_back.get_height()/2 - self.move_distance) )
                
                super().draw(win)
                win.blit(shooter_imgs_front,(self.x-shooter_imgs_front.get_width()/2,self.y-shooter_imgs_front.get_height()/2 + height_diff - self.move_distance) )
                
                win.blit(self.stone_imgs[0],(self.x-self.stone_imgs[0].get_width()/2,self.y-self.stone_imgs[0].get_height()/2 - height_diff2 - self.move_distance) )
                
                # if enemy not in range of there is a pause
                if not self.inrange or self.pause:
                    self.move_distance = 0
                else:
                    self.move_distance += self.attack_F         # to achieve the aacceleration effect
            else:
                self.move_distance = 0
        
        
        
    # attack the enemy and return the number of money when kill an enemy
    def attack(self, enemies):
        self.inrange = False
        enemy_closest = []
        
        # put every enemys in range into a list
        for en in enemies:
            x = en.x
            y = en.y
            
            dis = math.sqrt( (self.x-x)**2 + (self.y-y)**2 )
            
            if dis <= self.range:
                self.inrange = True
                enemy_closest.append(en)
            
        # choose the closest enemy
        enemy_closest.sort(key = lambda x: x.x)
        if len(enemy_closest)>0:
            first_en = enemy_closest[0]

            # only if the shoot is move to the top
            if self.move_distance >= 50:
                # check if the game is muted
                if self.music == True:
                    if self.name == "StoneTower1":
                        tower_sound1.play()
                    elif self.name == "StoneTower2":
                        tower_sound2.play()
                # if kill an enemy
                if first_en.get_hit(self.damage) ==True:
                    enemies.remove(first_en)
                    return first_en.money
      
        


        
    
        




tower2_imgs = []
shooter2_imgs=[]
stone2_imgs =[]


    
for x in range(3):
    add_str = str(x)
    tower2_imgs.append(
                pygame.transform.scale(
                        pygame.image.load(
                                        os.path.join("game_assets/stone_towers/stonetower2/foundation", add_str + ".png")
                                        ) 
                ,(64,64)
                )
                            
        )


for x in range(6):
    add_str = str(x)
    shooter2_imgs.append(
                pygame.transform.scale(
                        pygame.image.load(
                                        os.path.join("game_assets/stone_towers/stonetower2/shooter", add_str + ".png")
                                        ) 
                ,(64,14)
                )
                            
        )
    
for x in range(1):
    add_str = str(x)
    stone2_imgs.append(
                pygame.transform.scale(
                        pygame.image.load(
                                        os.path.join("game_assets/stone_towers/stonetower2/stone", add_str + ".png")
                                        ) 
                ,(15,15)
                )
                            
        )    



class StoneTower2(StoneTower1):
    def __init__(self,x,y):
        super().__init__(x, y)
        self.tower_imgs=tower2_imgs[:]
        self.shooter_imgs=shooter2_imgs[:]
        self.stone_imgs =stone2_imgs[:]
        self.stone_count = 0

        self.range = 80


        self.attack_F = 1
        self.damage = 2
        self.original_damage = 2
        self.buy_price = 700
        self.name = "StoneTower2"
        self.music = True
        self.max_health=15
        self.health = self.max_health
        



















        