

import pygame
import os
import time
import random
# import assets

from enemies.scorpion import Scorpion,Scorpion_map2,Scorpion_map3
from enemies.wizard import Wizard,Wizard_map2,Wizard_map3
from enemies.goblin import Goblin,Goblin_map2,Goblin_map3
from enemies.warrior import Warrior,Warrior_map2,Warrior_map3
from towers.stoneTower import StoneTower1,StoneTower2
from towers.supportTower import RangeTower,DamageTower
from menu.purchase_menu import Purchase_Menu
from menu.menu import Menu_horizontial,Button


lives_img = pygame.transform.scale(pygame.image.load(os.path.join("game_assets","heart.png")) , (64,64))
star_img_big = pygame.transform.scale(
                    pygame.image.load (os.path.join("game_assets/menu","star.png" ))
                    ,(35,35)
                    )
attackT1_btn = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","attack_tower1.png"))
                                 ,(60,60)
                                 )
attackT2_btn = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","attack_tower2.png"))
                                 ,(60,60)
                                 )
rangeT_btn = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","range_tower.png"))
                                 ,(60,60)
                                 )
damageT_btn = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","damage_tower.png"))
                                 ,(60,60)
                                 )
star_img_small = pygame.transform.scale(
                    pygame.image.load (os.path.join("game_assets/menu","star.png" ))
                    ,(25,25)
                    )

menu_bg = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","menu.png"))
                                 ,(120,55)
                                 )
button_upgrade = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","upgrade.png"))
                                 ,(50,50)
                                 )

sell_btn = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","sell.png"))
                                 ,(50,50)
                                 )

button_pause = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_pause.png"))
                                 ,(60,60)
                                 )

button_music = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_music.png"))
                                 ,(60,60)
                                 )

button_music_off = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_music_off.png"))
                                 ,(60,60)
                                 )


button_start = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_start.png"))
                                 ,(60,60)
                                 )

button_quick = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","button_quick.png"))
                                 ,(60,60)
                                 )

wave_table = pygame.transform.scale(
                    pygame.image.load(os.path.join("game_assets/menu","wave_table.png"))
                                 ,(165,100)
                                 )

# create music button
music_btn = Button(185, 540, button_music, "button_music")

# create music_off button 
music_off_btn = Button(185, 540, button_music_off, "button_music_off")


# default starting condition: currency, lives
default_life = 3
default_currency = 1500


# game aethetics (fonts, char_size)
gm_win_w = 900
gm_win_h = 600


pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.music.load("./game_assets/music/bgmusic.mp3")

class Game:
    def __init__(self):
        self.width = gm_win_w                      # Window Size
        self.height = gm_win_h
        
        self.win=pygame.display.set_mode((self.width,self.height))      
        self.enemys = []                     # enemy list saves tuples of locations on the maps
        self.attack_towers = []              # attack tower list

        self.support_towers = []            # suppport tower list
        self.purchase_menus = []            # purchase menu list
        self.buttons = []                   # button list
        self.lives = default_life  
        self.currency = default_currency                   
        self.life_font = pygame.font.SysFont("name", 50)
        self.currency_font = pygame.font.SysFont("name", 50)
        self.bg = pygame.image.load(os.path.join("game_assets", "bg.png"))      # game background from the asset folder
        self.bg = pygame.transform.scale(self.bg, (self.width,self.height))     # to change the scale of game background
        self.clicks = []                   # list to save mouse clicking actions
        self.timer1=time.time()            # timer 1 - used to calculate the time of enemy generation in background
        self.timer2=time.time()            # timer 2 - userd to calculate the wave time


        self.selected_tower = None         # save selected towers
        self.adding_tower= False           # a flag to check if the user is purchasing a tower
        self.adding_tower_type=None        # used to check if we purchase a wrong tower, users can click a correct one after
        self.main_pause = False            # flag
        


        self.wave_font = pygame.font.SysFont("name", 35)
        
        self.quick_level = 1              
        
        self.change_wave = True           # flag
        self.cur_wave = 0                 
        self.wave_speed=[1,2,3]           # the more difficult the game is, the faster the enemy comes out, wait to complish
        self.wave_speed_original=[1,2,3]  
        self.enemy_waitadd = None         # keeps the enemys in the background
        self.wave_start = False           # flag used to check if the next enemy should come out
        self.addenemy_end = False         # checks if all the enemy has come out
        self.score = 0                    # the score player gets
        self.score_font = pygame.font.SysFont("name", 35)
        self.level=1
        self.music = True                 # enable music by default          
        self.wave = [
        
                        [ 5 , 5 ,0 ,0],
                        [ 5 , 5 ,5 ,0],
                        [ 0 , 10 ,10 ,0],
                        [ 5 , 10 ,10 ,5],
                        [ 0 , 7 ,7 ,6],
       
                        
                    ]
        self.background_music = pygame.mixer.Sound("./game_assets/music/bgmusic.mp3")

        
        
    # draw eveything in the following:
    # the location tuple of mouse is used to drag towers around on the map   
        
    def draw(self,move_x,move_y):
        
        # draw background
        self.win.blit(self.bg, (0,0))
      
       ### draw enemys - referenced to the tutorial online (links on the decription sheets) 
        for en in self.enemys:
            en.draw(self.win)
            #  drawing the path of enemy, use to program
            # for p in en.path:
            #     pygame.draw.circle(self.win, (255,0,0), (p[0],p[1]), 5)
        
       # draw attack_tower        
        for tw in self.attack_towers:
            tw.draw(self.win,move_x,move_y)
            
            
       # draw support_tower             
        for tw in self.support_towers:
            tw.draw(self.win,move_x,move_y)
            
            
        # draw lives
        text_life = self.life_font.render(str(self.lives), 1, (255,255,255))
        life = lives_img
        self.win.blit(life, (self.width-life.get_width(),5))
        self.win.blit(text_life, (self.width-life.get_width()-text_life.get_width(),20))
                
    
        # draw currency
        text_money = self.life_font.render(str(self.currency), 1, (255,255,255))
        money = star_img_big
        self.win.blit(money, (self.width-life.get_width()+20,60))
        self.win.blit(text_money, (self.width-money.get_width()-text_money.get_width()-20,60))
        
        # draw purchase menu
        for p_menu in self.purchase_menus:
            p_menu.draw(self.win)
            
        # draw bottons
        for btn in self.buttons:
            btn.draw(self.win)    
            
        # draw wave_table and score
        text_wave = self.wave_font.render("wave "+str(self.cur_wave+1), 1, (255,255,255))
        text_score = self.score_font.render("score: "+str(self.score), 1, (255,255,255))
        self.win.blit(wave_table, (20,20))
        self.win.blit(text_wave, (30,30))
        self.win.blit(text_score, (30,75))
        
        
        
        
        pygame.display.update()
        
        
 
        
 
                            
                        
    # Building Towers
    # Depending on what user clicks, append a tower on the (x,y) location on the map
             
    def add_tower(self,button_name,X,Y):
        button_type = ["attackT1","attackT2","rangeT","damageT"]
        for i in range(len(button_type)):
            if button_type[i] == button_name:
                if i==0 or i==1:
                    if i==0:
                        self.attack_towers.append(StoneTower1(X, Y))
                    elif i==1:
                        self.attack_towers.append(StoneTower2(X, Y))
                        
                   # turn off the function of showing upgrade/ destroy function here
                    self.attack_towers[-1].before_put=True
                    
                    # record the currenct selected tower
                    self.adding_tower_type = "a"
                    
                    # pause the attack/ support tower function 
                    if self.main_pause:
                        self.attack_towers[-1].pause = True                  
                elif i==2 or i==3:
                    if i==2:
                        self.support_towers.append(RangeTower(X, Y))
                    elif i==3:
                        self.support_towers.append(DamageTower(X, Y))
                    self.adding_tower_type = "s"
                    self.support_towers[-1].before_put=True
                   
                    
    # Placement of tower
    def put_tower(self,X,Y):
        if self.adding_tower_type == "a":
            tower=self.attack_towers[-1]
            # if users clicks on the quick level function, tower attack spped will be timed by the quick level 
            tower.attack_F  = tower.attack_F_original * self.quick_level   # new attack tower speed initialize according to speed level
            
            # purchasing successfully, currency deducted.
            self.currency -= tower.buy_price
        elif self.adding_tower_type == "s":   
            tower=self.support_towers[-1]
            self.currency -= tower.buy_price
        # restore before_put function to allow upgrading function and destroy function.
        # tower is built on (x, y)
        tower.before_put = False
        tower.x = X
        tower.y = Y
        tower.menu = Menu_horizontial(tower,X, Y-70, menu_bg)
        if self.adding_tower_type == "a":
            tower.menu.add_btn(button_upgrade,"Upgrade",[250,500,"Max"],star_img_small)
            tower.menu.add_btn(sell_btn,"Sell",[250,375,625],star_img_small)
            # add the tower sound track to the new tower：
            if self.music == False:
                tower.music = False
        elif self.adding_tower_type == "s": 
            tower.menu.add_btn(button_upgrade,"Upgrade",[150,"Max"],star_img_small)
            tower.menu.add_btn(sell_btn,"Sell",[150,225],star_img_small)
            
        


        self.adding_tower_type = None
        self.adding_tower = False
        
        
        
    def add_enemy(self):
        speed = self.wave_speed[0]               
        en_show_interval = 1                     # time interval of each enemy
        en_wave_interval = 10                    # time interval of each wave

        if self.change_wave == True :            # New enemy comes if the last wave of enemys is finished
            if time.time() - self.timer2 >=  en_wave_interval/speed:        # check if it is the time that next wave of enemies should show 
                self.enemy_waitadd = self.wave[self.cur_wave][:]            # put the next wave of enemies into wait list 
                self.wave_start = True                                      # next wave starts
        
        if not self.main_pause and self.cur_wave < len(self.wave):               # if current wave is not the last wave and there is not a pause 

            if self.wave_start == True:                                       # if the next wave start 
                if time.time()-self.timer1 >= en_show_interval/speed:         # count time to make sure there is a short period of time between every single enemy
                
                    # if this wave has not finished
                    if sum(self.enemy_waitadd) != 0:                        
                        self.change_wave = False                             
                        
                        # enemy awaited is decreased as it come out to the map
                        if self.level == 1:
                        
                            en = random.choice([Scorpion(), Wizard(), Goblin(),Warrior()])            # 新的敌人从三种敌人中随机选一个
                        elif self.level == 2:
                            en = random.choice([Scorpion_map2(), Wizard_map2(), Goblin_map2(),Warrior_map2()])  # 新的敌人从三种敌人中随机选一个
                        elif  self.level == 3:
                            en = random.choice([Scorpion_map3(), Wizard_map3(), Goblin_map3(),Warrior_map3()])  # 新的敌人从三种敌人中随机选一个
                        en.vel = en.vel_original * self.quick_level                                         # new enemy speed up
                        if self.music == False:                                                              # new enemy set music mode
                            en.music = False
                            
                            
                        # enemy awaited is decreased as it come out to the map
                        if en.name == "scorpion":                             
                            if self.enemy_waitadd[0] == 0:
                                return
                            else:
                                self.enemy_waitadd[0] -= 1
                        elif en.name == "wizard":
                            if self.enemy_waitadd[1] == 0:
                                return
                            else:
                                self.enemy_waitadd[1] -= 1
                        elif en.name == "goblin":
                            if self.enemy_waitadd[2] == 0:
                                return
                            else:
                                self.enemy_waitadd[2] -= 1
                        elif en.name == "warrior":
                            if self.enemy_waitadd[3] == 0:
                                return
                            else:
                                self.enemy_waitadd[3] -= 1                        
                            
                        self.enemys.append(en)               # new enemies is added to the game (en)
                        print(en)
                        self.timer1=time.time()             # reset timers
                            
                    # Wave ends if the enemy is equal to zero
                    elif sum(self.enemy_waitadd) == 0: 
                        # if the currentwave+1 isnt equal to the total wave, it waits till the enemy all come out.
                        # new wave will be held
                        if self.cur_wave +1 < len(self.wave):  
                            self.change_wave = True            
                            self.cur_wave += 1                 
                            self.timer2=time.time()          
                            self.wave_start = False          
                        else:
                            self.addenemy_end = True        


    def game_init(self):
        # Building purchase menue with items- 2 attakc towers, and 2 supportive towers
        purmenu = Purchase_Menu(860,250)
        purmenu.menu.add_btn(attackT1_btn, "attackT1",[ StoneTower1(0,0).buy_price ],star_img_small)
        purmenu.menu.add_btn(attackT2_btn, "attackT2",[StoneTower2(0,0).buy_price ],star_img_small)
        purmenu.menu.add_btn(rangeT_btn, "rangeT",[ RangeTower(0,0).buy_price ],star_img_small)
        purmenu.menu.add_btn(damageT_btn, "damageT",[ DamageTower(0,0).buy_price],star_img_small)

        # Create pause, start, quick, sound button.
        pause_btn = Button(20, 540, button_pause, "button_pause")
        start_btn = Button(75, 540, button_start, "button_start")
        
        
        # create speed up button
        quick_btn = Button(130, 540, button_quick, "button_quick")
        
        # create music button
        music_btn = Button(185, 540, button_music, "button_music")
        

        
        
        self.purchase_menus.append(purmenu)
        self.buttons.append(pause_btn)
        self.buttons.append(start_btn)
        self.buttons.append(quick_btn)
        self.buttons.append(music_btn)

        
        
                
        
        
        
        
        
        
    # Main loop
    def run(self):
        
        # bgm start
        self.background_music.play(-1)
        run = True
        clock = pygame.time.Clock()
        

        while run:

            clock.tick(60)
            for event in pygame.event.get():   
                if event.type == pygame.QUIT:
                    run = False
                    
                pos = pygame.mouse.get_pos()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicks.append((pos[0],pos[1]))
                    print((pos[0],pos[1]))
                    
                    # Purchasing Towers
                    
                    btn_clicked_P = None        

                    for intf in self.purchase_menus:                                   # View the purchasing menu
                        btn_clicked_P = intf.menu.get_clicked(pos[0],pos[1])           # record the mouse location if any item is being clicked 
                        
                        # if user clicks on the purchase menu
                        if btn_clicked_P:
                            print(btn_clicked_P)  
                            
                            cost = intf.menu.get_upgrade_cost(btn_clicked_P)      
                            if self.currency >= cost:                                # check if the user has sufficient amount 
                                
                                # if user has not yet decided where to place the tower, tower follows the mouse
                                
                                if self.adding_tower == False:
                                    self.adding_tower = True
                                    self.add_tower(btn_clicked_P,pos[0],pos[1])  
                                    
                                # if user clicks on a different tower, it switches to one another
                                
                                else:
                                    if self.adding_tower_type == "a":
                                        del(self.attack_towers[-1])
                                        self.adding_tower_type = None
    
                                        self.add_tower(btn_clicked_P,pos[0],pos[1])
    
                                    elif self.adding_tower_type == "s":
                                        del(self.support_towers[-1])
                                        self.adding_tower_type = None
    
                                        self.add_tower(btn_clicked_P,pos[0],pos[1])
                    
                     # as user clicks on the tower, it waits the next action
                    if btn_clicked_P != None:
                        continue
                                    
                                
                                
                    # To upgrade or sell the tower
                    btn_clicked_T = None
                    
                     # if there's a tower is selected
                    if self.selected_tower :
                        btn_clicked_T=self.selected_tower.menu.get_clicked(pos[0],pos[1])
                        if btn_clicked_T:
                            print(btn_clicked_T)
                            
                            # click upgrade button to upgrade
                            if btn_clicked_T == "Upgrade":
                                cost = self.selected_tower.menu.get_upgrade_cost(btn_clicked_T)
                                
                                # as the maximum level of tower is a str, we cannot do math calculation with int.
                                # we applied a try/except to ignore the request here                                
                                try:
                                    ifwork = self.currency >= cost
                                except TypeError:
                                    pass
                                else:
                                    if ifwork == True:
                                        self.selected_tower.upgrade()         # tower gets upgraded if theres no error
                                        self.currency -= cost  
                            # To sell the tower
                            elif btn_clicked_T == "Sell":
                                get_money = self.selected_tower.menu.get_sell_money(btn_clicked_T)
                                self.currency += get_money
                                self.selected_tower = None
                                
                                
                                
                                
                    
                    # check if any supportive and attack tower is being clicked, it will be added to selected items
                    # if function is applied here to make sure it shows upgrade functions continuously after upgrading
                    if not btn_clicked_T and not self.adding_tower:
                        for tw in self.attack_towers:
                            if tw.click(pos[0],pos[1]):
                                tw.selected = True                     # To show the upgrading menu (referred to tower.py file)
                                self.selected_tower=tw
                            else:
                                tw.selected = False 
                                
                        for tw in self.support_towers:
                            if tw.click(pos[0],pos[1]):
                                tw.selected = True
                                self.selected_tower=tw
                            else:
                                tw.selected = False
                  
                    # Placing tower
                    if self.adding_tower== True:
                        self.put_tower(pos[0], pos[1])
                        
                        
                        
                    # button click on speed, pause...
                    btn_clicked_B = None
        
                    # check if its being clicked
                    for btn in self.buttons:
                        btn_clicked_B = btn.click(pos[0], pos[1])
                        
                        # pause
                        if btn_clicked_B == "button_pause":
                            self.main_pause = True          # pause the generation of enemy and tower action
                            
                            # pause the action of towers and enemy
                            for tw in self.attack_towers:
                                tw.pause = True
                            for en in self.enemys:
                                en.pause = True
                            print(btn_clicked_B)
                            
                        # start
                        # make the main_pause = false to continue actions (reverse the previous action)
                        elif btn_clicked_B == "button_start":
                            self.main_pause = False                            
                            for tw in self.attack_towers:
                                tw.pause = False
                            for en in self.enemys:
                                en.pause = False                       
                                print(btn_clicked_B)
                        #Accelerate
    
                        elif btn_clicked_B == "button_quick":
                            
                            # if the speed exceed level 3, it jumps back to level 1
                            if self.quick_level <=2:
                                self.quick_level+=1
                            else:
                                self.quick_level = 1
                            
                            # accelerate the tower/ enemy speed/ and shorten the interval of wave by different level
                            for tw in self.attack_towers:
                                tw.attack_F = tw.attack_F_original * self.quick_level
                            
                            
                            for en in self.enemys:
                                en.vel = en.vel_original * self.quick_level
                            
                            
                            for s in range(len(self.wave_speed)):
                                self.wave_speed[s] = self.wave_speed_original[s] * self.quick_level

                            print(f"{btn_clicked_B},quick_level:{self.quick_level}")
                            
                            
                            
                            
                        # stop or start music
                        
                        elif btn_clicked_B == "button_music":
                            self.music = False
                            self.background_music.stop()
                            self.buttons.remove(btn)
                            self.buttons.append(music_off_btn)

                            
                        elif btn_clicked_B== "button_music_off":
                            self.music = True
                            self.background_music.play()
                            self.buttons.remove(btn)
                            self.buttons.append(music_btn)
                        
                        
                        
                               
            # Adding enemies
            # if enemies are not added completed to the game. it keeps adding--
            if self.addenemy_end == False:
                self.add_enemy()   #添加敌人

            # enemy sounds
            for en in self.enemys:
                if self.music == False:
                    en.music = False
                elif self.music == True:
                    en.music = True
            # touwer sounds
            for tw in self.attack_towers:
                if self.music == False:
                    tw.music = False
                elif self.music == True:
                    tw.music = True                    
                             
                
            
            # If enemy arrives to the end, we deduct the live by 1, score by 10
            
            # to_del is used to record enemy that needed to be deleted
            to_del = []
            # if enemy has gone out of the bundary, it is added to the list and excute the deduction 
            for en in self.enemys:
                if en.x <= -15 or en.x >= 915 or en.y>=615:
                    to_del.append(en)
                    self.lives -= 1
                    self.score -= 10
            
            # 遍历待删除数组，从敌人数组中删除其中的元素
            for en in to_del:
                self.enemys.remove(en)
                
            # if tower is no longer exist, it is removed 
            # or we use to attack function to earn money and score   
            for tw in self.attack_towers:
                if tw.exist == False:
                    self.attack_towers.remove(tw)
                else:
                    get_money = tw.attack(self.enemys)
                    if type(get_money) == int:
                        self.currency += get_money * 20
                        self.score += get_money
                    
                    
            # similiar to the above
            for tw in self.support_towers:
                if tw.exist == False:
                    self.support_towers.remove(tw)
                else:
                    tw.support(self.attack_towers)
            

            # iterate all the enemys, if it is a boss,launch an attack towards to tower
            for en in self.enemys:
                if en.type == "boss":
                    tw_distroyed = en.attack(self.attack_towers,self.support_towers)
                    if tw_distroyed != None:
                        if tw_distroyed.type == "attack_tower":
                            self.attack_towers.remove(tw_distroyed)
                        elif tw_distroyed.type == "support_tower":
                            self.support_towers.remove(tw_distroyed)
            
            # if the live =0, you lose，return false and go to the end level menu
            if self.lives <= 0:
                print("you lose")
                # reset the score
                self.score=0
                # stop the music of this map
                self.background_music.stop()
                return False
                
            # if enemy = 0, you win 
            if self.addenemy_end == True and self.enemys == []:
                print("you win")
                self.background_music.stop()
                return True
            # draw every in this game 
            self.draw(pos[0],pos[1])
            
        pygame.quit()
                




# game of map2
class Game_2(Game):
    def __init__(self):
        super().__init__()
        self.bg = pygame.image.load(os.path.join("game_assets", "bg2.png"))  # 游戏界面背景图
        self.bg = pygame.transform.scale(self.bg, (self.width,self.height)) # 改背景图尺寸
        self.level =2 
        
        
    


# game of map3
class Game_3(Game):
    def __init__(self):
        super().__init__()
        self.bg = pygame.image.load(os.path.join("game_assets", "bg3.png"))  # 游戏界面背景图
        self.bg = pygame.transform.scale(self.bg, (self.width,self.height)) # 改背景图尺寸
        self.level = 3






        
       
        
        