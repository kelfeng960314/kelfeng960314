# -*- coding: utf-8 -*-


import pygame
import math
import os  


pygame.mixer.init()

# set different sound when enemy was defeated
s1=pygame.mixer.Sound("./game_assets/music/monsterDeadth.mp3")
s2=pygame.mixer.Sound("./game_assets/music/wizardDeadth.mp3")            
s3=pygame.mixer.Sound("./game_assets/music/goblinDeadth.mp3")    
# set volumn
s1.set_volume(0.3)
s2.set_volume(0.3)
s3.set_volume(0.3)


# create an enemy class
class Enemy:

    def __init__(self):

        self.width=64
        self.height=64
        self.animation_count=0
        self.health = 1                            
        self.vel = 1                                 # the speed of the enemy
        self.vel_original = 1
        #  the path, each map is different
        self.path = [(-10,192),(21, 192), (99, 191), (155, 215), (196, 241), (393, 242), (448, 197), (466, 109), (514, 60), (577, 53), (615, 94), (634, 201), (685, 244), (746, 251), (785, 330), (759, 399), (719, 431), (573, 435), (521, 466), (150, 473), (75, 422), (54, 323), (2, 289)]
        
        self.x=self.path[0][0]
        self.y=self.path[0][1]
        
        self.imgs = []                         
        # path index
        self.path_pos = 0           
        # to check the direction of move, to achieve change direction animation
        self.left_to_right = True
        self.right_to_left = False
        self.pause = False
        self.music = True
        self.type = "normal_enemy"
        
    # draw enemy
    def draw(self, win):
        
        
        self.draw_health_bar(win)
        if not self.pause:
            self.move()
        
        # used animation count function to show movements
        win.blit(self.imgs[self.animation_count], (self.x-self.imgs[self.animation_count].get_width()/2,
                                                   self.y-self.imgs[self.animation_count].get_height()/2))
    
    # move enemy
    # mostly used tutorial video as reference here and have improved it, please view the description page
    def move(self):    
        
        # repeating animation
        self.animation_count += 1
        if self.type == "boss":
            self.animation_count2 += 1
            if self.animation_count2 >= len(self.imgs_attack):
                self.can_attack = True
                self.animation_count2 = 0

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

            
        # x1, y1 is set as the current position  x2,y2 is the next
        
        x1,y1 = self.path[self.path_pos]
        
        # we manually input the final point out the map
        if self.path_pos + 1 >= len(self.path):
            if self.map == 1:            
                x2,y2=(-15,286)
            elif self.map ==2:
                x2,y2=(831,615)
            elif self.map ==3:
                x2,y2=(915,77)                
        else:
            x2, y2 = self.path[self.path_pos+1]
        
        # we then calculate the length, and the slope of 2 points (x1,y1) -> (x2,y2)
        length = math.sqrt( (x2-x1)**2 + (y2-y1)**2 )
        dirn = ((x2-x1)/length,(y2-y1)/length)
        
        # if dirn[0]<0 enmies walks from the right to the left
        if dirn[0]<0 and self.left_to_right:
            self.left_to_right = False
            self.right_to_left = True
            for i,img in enumerate(self.imgs):
                    self.imgs[i] = pygame.transform.flip(self.imgs[i],True,False)
        # if dirn[0]>0 enmies walks from the left to the right 
        elif dirn[0]>0 and self.right_to_left:
            self.left_to_right = True
            self.right_to_left = False
                     
            for i,img in enumerate(self.imgs):
                self.imgs[i] = pygame.transform.flip(self.imgs[i],True,False)
            
        # calculate the next step (*acceleration)
        move_x,move_y = ((self.x+dirn[0]*self.vel),(self.y+dirn[1]*self.vel))
        
        # update the position
        self.x=move_x
        self.y=move_y
        print("current coordinate：",end="")
        print(round(self.x),round(self.y))
        print("the previous coordinate：",end="")
        print(x1,y1)
        print("the next coordinate",end="")
        print(x2,y2)
        
        
        
        # If function to check if enemy arrive from x1, y1, to x2, y2
        
        if dirn[0]>=0:                              # From left to the right
            if dirn[1] >=0:                         # From top left to bottom right
                if self.x>=x2 and self.y>=y2:
                    if self.path_pos + 1 < len(self.path):
                        self.path_pos +=1
            else:                                   # from bottom left to top right
                if self.x>=x2 and self.y<=y2:
                    if self.path_pos + 1 < len(self.path):
                        self.path_pos +=1   
        else:                                        # from right to left
            if dirn[1] >=0:                         # from top right to bottom left
                if self.x<=x2 and self.y>=y2:
                    if self.path_pos + 1 < len(self.path):
                        self.path_pos +=1
            else:                                   # from bottom right to top right 
                if self.x<=x2 and self.y<=y2:
                    if self.path_pos + 1 < len(self.path):
                        self.path_pos +=1                       
                
            
            
            
    # draw health bar
    def draw_health_bar(self,win):
        length = 50
        move_by = length /self.max_health
        health_bar = move_by * self.health
        
        pygame.draw.rect(win , (255,0,0),(self.x-10,self.y-25 , length , 7))
        pygame.draw.rect(win , (0,255,0),(self.x-10,self.y-25 , health_bar , 7))

    # when enemy get hurt, if killed,return True 
    def get_hit(self,damage):
        
        self.health -=damage
        if self.health <=0:
            if self.music == True:
                if self.name == "scorpion":
                    s1.play()
                elif self.name == "wizard":
                    s2.play()
                elif self.name == "goblin":
                    s3.play()
                
            return True
        return False
    
    
    

    
    
    
    
   
    
    
# create the enemy class of diffenert map 
class Enemy_map2(Enemy):
    def __init__(self):
        super().__init__()
        self.path = [(17, 452),(69, 452),(109, 441),(137, 407),(156, 336), (175, 296), (208, 274),(245, 264),(285, 243),(306, 205),(314, 154),(328, 121),(358, 87),(402, 76),(543, 75),(616, 55),(682, 73),(768, 76),(810, 104),(828, 156),(831, 202),(806, 238),(758, 261),(704, 290),(679, 341),(682, 398),(722, 442),(774, 456),(807, 486),(828, 536),(831, 582)]
        self.x=self.path[0][0]
        self.y=self.path[0][1]
        
        
        
class Enemy_map3(Enemy):
    def __init__(self):
        super().__init__()
        self.path = [(21, 408),(89, 409),(142, 421),(194, 454),(262, 438),(323, 457),(491, 459),(580, 382),(529, 275),(463, 268),(364, 265),(320, 227),(303, 159),(325, 110),(379, 83),(428, 81),(869, 77)]
        self.x=self.path[0][0]
        self.y=self.path[0][1]

    
    
    
    
# create the boss class which will attack the tower
class Boss(Enemy):
    def __init__(self):
        super().__init__()
        self.inrange = False

        self.imgs_attack = []

        self.animation_count2 = 0
        self.type = "boss"
        self.can_attack=False
        
        
    def draw(self, win):
        self.draw_health_bar(win)
        if not self.pause:
            self.move()
        if self.inrange:
            win.blit(self.imgs_attack[self.animation_count2], (self.x-self.imgs[self.animation_count].get_width()/2,
                                           self.y-self.imgs[self.animation_count].get_height()/2))
        else:
            self.animation_count2 = 0
            win.blit(self.imgs[self.animation_count], (self.x-self.imgs[self.animation_count].get_width()/2,
                                                   self.y-self.imgs[self.animation_count].get_height()/2))
            
    # attack the tower which is in range 
    def attack(self, attack_towers,support_towers):
        self.inrange = False
        towers = attack_towers + support_towers 
        tower_closest = []
        
        # put the tower which is in range into the list
        for tw in towers:
            x = tw.x
            y = tw.y
            
            dis = math.sqrt( (self.x-x)**2 + (self.y-y)**2 )
            
            if dis <= self.range:
                self.inrange = True
                tower_closest.append(tw)
            
        # choose the closest tower
        tower_closest.sort(key = lambda x: x.x)
        if len(tower_closest)>0:
            first_tw = tower_closest[0]
            # only if it is the end of the attack animation, the boss will attack
            if self.can_attack:
                if first_tw.get_hit(self.damage) == True:
                    self.can_attack=False
                    return first_tw
            

# create the boss class of different map
class Boss_map2(Boss):
    def __init__(self):
        super().__init__()
        self.path = [(17, 452),(69, 452),(109, 441),(137, 407),(156, 336), (175, 296), (208, 274),(245, 264),(285, 243),(306, 205),(314, 154),(328, 121),(358, 87),(402, 76),(543, 75),(616, 55),(682, 73),(768, 76),(810, 104),(828, 156),(831, 202),(806, 238),(758, 261),(704, 290),(679, 341),(682, 398),(722, 442),(774, 456),(807, 486),(828, 536),(831, 582)]
        self.x=self.path[0][0]
        self.y=self.path[0][1]

    

class Boss_map3(Boss):
    def __init__(self):
        super().__init__()
        self.path = [(21, 408),(89, 409),(142, 421),(194, 454),(262, 438),(323, 457),(491, 459),(580, 382),(529, 275),(463, 268),(364, 265),(320, 227),(303, 159),(325, 110),(379, 83),(428, 81),(869, 77)]
        self.x=self.path[0][0]
        self.y=self.path[0][1]


        
        
        
        
        
        
        

        