# -*- coding: utf-8 -*-


import pygame
import os 
pygame.init()
pygame.font.init()













# create a button class, use to stop/start game mute music...

class Button:
    def __init__(self,x,y,img,name):
        self.name=name
        self.img=img
        self.x=x
        self.y=y
        self.width = self.img.get_width()
        self.height = self.img.get_height()


    # if the button get clicked,return true
    def click(self,X,Y):
        if X<=self.x + self.width and X>=self.x:
            if Y<=self.y+self.height and Y >= self.y:
                return self.name
        return False
    # draw the picture of this button
    def draw(self,win):
        win.blit(self.img, (self.x,self.y))       
       




# create a Button_tower class,used to upgrade or purchase tower

class Button_tower(Button):
    def __init__(self,tower,x,y,img,name,item_cost,star_img):
        super().__init__(x, y, img, name)
        
        self.font = pygame.font.SysFont("number", 25 )
        self.tower = tower
        self.star_img = star_img
        self.item_cost = item_cost[:]
        self.star_width = star_img.get_width()
        self.star_height = star_img.get_height()  
        
    
    def draw(self,win):
        super().draw(win)
        # draw the picture of button,money number needed to buy or upgrade a tower and money picture
        win.blit(self.star_img,(self.x ,self.y+50))           
        text = self.font.render(str(self.item_cost[self.tower.level-1]), 1, (255,255,255))
        win.blit(text,(self.x+self.star_width ,self.y+50))

        


# The horizontal menu, can be accessed through add_ BTN add keys and arrange them horizontally to the right for the upgrade menu of the tower
class Menu_horizontial:
    def __init__(self,tower,x,y,img):
        self.x = x
        self.y = y
        # 获得此菜单图片的宽高
        self.width = img.get_width()        
        self.height = img.get_height()
        
        self.items = 0             # the number of button of this menu
        self.bg=img               
        self.buttons = []           # the list of button

        self.tower=tower         
        self.top_left = (self.x-self.width/2,self.y-self.height/2)          # Calculate the top left point of this menu
        self.center=(self.x,self.y)                                         # Calculate the center point of this menu
        self.far_left = self.top_left[0]                                    # Calculate the center point of the menu and take the leftmost point of the menu
        self.far_top = self.top_left[1]                                     # Take the top point of this menu
        
    # add button function, used to buy or upgrade a tower
    def add_btn(self,img,name,item_cost,star_img):                
            self.items += 1
            button_width = img.get_width()
            button_height = img.get_height() 
            
            # Calculate the X and Y coordinates of the newly added key through self The items control is arranged horizontally to the right
            btn_x =self.far_left + 7*self.items + (self.items-1) * button_width         
            btn_y =self.far_top + 5   
            self.buttons.append(Button_tower(self.tower,btn_x,btn_y,img,name,item_cost,star_img))
            
            
    def draw(self,win):
        win.blit(self.bg, self.top_left)

        for item in self.buttons:
            item.draw(win)

    # when menu get clicked,check if there's a button get clicked,if is,return the name of button
    def get_clicked(self,X,Y):
        btn_clicked_B = None 
        for btn in self.buttons:
            btn_clicked_B = btn.click(X,Y)
            if  btn_clicked_B:
                return btn_clicked_B
        return None
    
    # return the money of upgrading a tower
    def get_upgrade_cost(self,button_name):
         for btn in self.buttons:
            if btn.name == button_name:       
                return btn.item_cost[self.tower.level-1]
     # return the moeny of selling a tower
    def get_sell_money(self,button_name):
         self.tower.exist = False
         return self.get_upgrade_cost(button_name)
            

# The vertical menu can be accessed through add_ BTN adds keys and arranges them vertically downward for the purchase menu of the tower
class Menu_vertical(Menu_horizontial): 
    def __init__(self,tower,x,y,img):           
        super().__init__(tower,x,y,img)
        
    def add_btn(self,img,name,item_cost,star_img):
            self.items += 1
            button_width = img.get_width()
            button_height = img.get_height()            
            btn_x =self.far_left +7
            btn_y =self.far_top + 14*self.items + (self.items-1) * button_height
            self.buttons.append(Button_tower(self.tower,btn_x,btn_y,img,name,item_cost,star_img))        
    
        
  
        
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
  
    
