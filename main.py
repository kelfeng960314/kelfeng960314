# -*- coding: utf-8 -*-

import pygame
import time


from game import Game,Game_2,Game_3
from menu.start_menu import Menu_Start
from menu.endlevel_menu import Menu_endlevel_win, Menu_endlevel_failed
from menu.scoreboard_menu import Menu_scoreboard



run=True
clock = pygame.time.Clock()

pygame.init()
pygame.font.init()
pygame.mixer.init()
# Background music sound track
pygame.mixer.music.load("./game_assets/music/bgmusic.mp3")
pygame.mixer.music.set_volume(0.7)
# pygame.mixer.music.load("./game_assets/music/bomb_sound.mp3")

# pygame.mixer.music.play()



clicks=[]
player_name=""








# Screen Size
win = pygame.display.set_mode((900,600))

# Starting Page/ VFinish Page (Win/Failed)
start_page = Menu_Start()
endlevel_page_win = Menu_endlevel_win()
endlevel_page_failed = Menu_endlevel_failed()
scoreboard_page = Menu_scoreboard()
scoreboard_page.update()




# Fonts / Color
score_font = pygame.font.SysFont("name", 50)
explain_font = pygame.font.SysFont("name", 30)
text_color = (255,255,255)

# Lines
text_finish = (450-122,220)
text_finish2 = (450-122,240)
text_finish3 = (450-122,260)
score_display = (450-100,180)
name_display = (375,280)

# Maximum length of input
max_name = 8



# Input functions for scoreboard
text_explain1 = explain_font.render("Please enter your name", 1, text_color)
text_explain2 = explain_font.render("Click 'Done' button to save", 1, text_color)
text_explain3 = explain_font.render("letters only", 1, text_color)

# Default level of the game, default score
level = 1
score = 0


def draw_levelmenu_text():
    win.blit(text_explain1, text_finish)
    win.blit(text_explain2, text_finish2)
    win.blit(text_explain3, text_finish3)  






# Game flow starts here: 
# Making Starting Page
start_page.draw(win)
pygame.display.update()


while run:
    # bgm start
    
    clock.tick(60)
    
    # 1. While loop/ for loop used to run the game unless a pleyer quits the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
            

                
        # 1-1. Saves clicking history of mouse
        pos = pygame.mouse.get_pos()   
        if event.type == pygame.MOUSEBUTTONDOWN:
                
            # prints our tuple of location (not meaningful to the game, but for development)
                
            clicks.append((pos[0],pos[1]))
            print((pos[0],pos[1]))
            
            # 1-2. Game starts to run when a user clicks on the play button
            
            btn_clicked_BM = None

            for btn in start_page.buttons:
                btn_clicked_BM = btn.click(pos[0], pos[1])
                if btn_clicked_BM == "button_play":
                    print(btn_clicked_BM)
                    
                    
                    


                    
                    # 1-3. Choose level of the game
                    while True :
                        
                        # we accumulate the score of each level
                        if level == 1:
                            game=Game()
                            game.game_init()
                            game.score = score
                        elif level ==2:
                            game=Game_2()
                            game.game_init()
                            game.score = score
                        elif level ==3:
                            game=Game_3()
                            game.game_init()  
                            game.score = score
                        
                        if game.run() == True:
                           
                           # score updating
                            score = game.score
                            
                            
                            # build a menu to show current socre
                            endlevel_page_win.draw(win)

                            text_score = score_font.render("score: "+str(score), 1, text_color)
                            win.blit(text_score, score_display)
                            draw_levelmenu_text()
                            pygame.display.update()
                            

                            # Waiting for actions on the menu
                            
                            menule_notclicked = True
                            
                            
                            # 1-4. Check what user clicks on the menu
                            while menule_notclicked:
                                
                                # No action
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                
                                    # Saves clicking action 
                                    pos = pygame.mouse.get_pos()   
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        btn_clicked_BM = None
                                        
                                        # showing up buttons in the menus
                                        for btn in endlevel_page_win.buttons:
                                            btn_clicked_BM = btn.click(pos[0], pos[1])
                                            
                                            # 1-5. If user clicks on the next level button, level goes up by 1
                                            if btn_clicked_BM == "button_right":
                                                print(btn_clicked_BM)
                                                menule_notclicked = False
                                                if level <=2:
                                                    level += 1
                                            
                                            # 1-6. users closed the program, window shuts down
                                            elif btn_clicked_BM == "button_close":
                                                print(btn_clicked_BM)
                                                pygame.quit()
                                                
                                            
                                            # 1-7. If user clicks on the save score button, current score is saved 
                                            elif btn_clicked_BM == "save_score":
                                                print(btn_clicked_BM)
                                                scoreboard = open('scoreboard.txt','a')
                                                scoreboard.write(f"{player_name.ljust(8)},{score}\n")
                                                a=" "
                                                scoreboard.write(f"{a.ljust(8)},0\n")
                                                scoreboard.close()
                                                scoreboard_page.update()    # 根据新添加记录更新排行榜
                                                
                                            # 1-8. If user clicks on the scoreboard, display scoreboard
                                            elif btn_clicked_BM == "button_scoreboard":
                                                print(btn_clicked_BM)
                                                
                                                # display scoreboard
                                                scoreboard_page.draw(win)
                                                pygame.display.update()
                                            
                                                menule_notclicked2 = True
                                                
                                                # Actions in the scoreboard menue
                                                while menule_notclicked2:
                                                    
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            pygame.quit()
                                                    
                                                        # Saving mouse actions
                                                        pos = pygame.mouse.get_pos()   
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            btn_clicked_BM2 = None
                                                            
                                                            # displaying scoreboard
                                                            for btn in scoreboard_page.buttons:
                                                                btn_clicked_BM2 = btn.click(pos[0], pos[1])
                                                                
                                                                # if user licks on close button, window close
                                                                if btn_clicked_BM2 == "button_close":
                                                                    print(btn_clicked_BM2)
                                                                    endlevel_page_win.draw(win)
                                                                    score_font = pygame.font.SysFont("name", 50)
                                                                    text_score = score_font.render("score: "+str(score), 1, (255,255,255))
                                                                    win.blit(text_score, score_display)
                                                                    draw_levelmenu_text()
                                                                    pygame.display.update()
                                                                    menule_notclicked2 = False
                                                                











                                                
                                                
                                                
                                            
                                            
                                
                                    # Keyboard functions when typing names to the scoreboard
                                    # 2. Enter players name
                                    if event.type == pygame.KEYDOWN:
                                        pygame.time.delay(15)
                                        
                                        # Checking value errors (Characters only)
                                        try:
                                            chr(event.key)
                                        except ValueError:
                                            continue
                                        
                                        else:
                                            # if user enters a backspace, the last digit [0:-1] will be removed
                                            if chr(event.key) == "\b":
                                                player_name = player_name[0:-1]
                                                # builds the scoreboard again
                                                endlevel_page_win.draw(win)
                                                win.blit(text_score, score_display)
                                                draw_levelmenu_text()                                                
                                                player_font = pygame.font.SysFont("name", 35)
                                                text_player = player_font.render(player_name, 1, text_color)
                                                win.blit(text_player, name_display)
                                                pygame.display.update() 
                                            else:
                                                if len(player_name) < max_name:
                                                    player_name += chr(event.key)
                                                    player_font = pygame.font.SysFont("name", 35)
                                                    text_player = player_font.render(player_name, 1, text_color)
                                                    win.blit(text_player, name_display)
                                                    pygame.display.update()                                 
                                    
                                    
                                    
    
                            
                         # 3 If players fails. 
                        else:
                            
                            score = game.score
                            
                            # 3-1. Display a failed result page
                            endlevel_page_failed.draw(win)
                            text_score = score_font.render("score: "+str(score), 1, text_color)
                            win.blit(text_score, score_display)
                            draw_levelmenu_text()                     
                            pygame.display.update()
                            
                            # Mouse actions
                            menule_notclicked = True
                            
                            # display the failed result
                            while menule_notclicked:
                                
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        pygame.quit()
                                
                                    pos = pygame.mouse.get_pos()  
                                    
                                    # mouse actions
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        # print(pos)
                                        btn_clicked_BM = None
                                        
                                        # 3-2. If users clicks on the restart button, game restart again
                                        for btn in endlevel_page_failed.buttons:
                                            btn_clicked_BM = btn.click(pos[0], pos[1])
                                            if btn_clicked_BM == "button_restart":
                                                print(btn_clicked_BM)
                                                menule_notclicked = False
                                                
                                            # 3-3. If user clicks on the close button, game shuts down
                                            elif btn_clicked_BM == "button_close":
                                                print(btn_clicked_BM)
                                                pygame.quit()  
                                                
                                            # 3-4. If users saves the score
                                            elif btn_clicked_BM == "save_score":
                                                print(btn_clicked_BM)
                                                # socre update in the txt file and display on the window
                                                scoreboard = open('scoreboard.txt','a')
                                                scoreboard.write(f"{player_name.ljust(8)},{score}\n")
                                                a=" "
                                                scoreboard.write(f"{a.ljust(8)},0\n")
                                                scoreboard.close()
                                                scoreboard_page.update()
                                                
                                            # 3-5. If users clicks on scoreboard, scoreboard is displayed
                                            elif btn_clicked_BM == "button_scoreboard":
                                                print(btn_clicked_BM)
                                                
                                                # display scoreboard
                                                scoreboard_page.draw(win)
                                                pygame.display.update()
                                                
                                                menule_notclicked2 = True
                                                
                                                # checks mouse action in the scoreboard
                                                while menule_notclicked2:
                                                    
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.QUIT:
                                                            pygame.quit()
                                                    
                                                        # saves mouse clicks
                                                        pos = pygame.mouse.get_pos()   
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            btn_clicked_BM2 = None
                                                            
                                                            # 3-6. If user clicks on the close button, closes scoreboard and saves current result
                                                            for btn in scoreboard_page.buttons:
                                                                btn_clicked_BM2 = btn.click(pos[0], pos[1])
                                                                if btn_clicked_BM2 == "button_close":
                                                                    print(btn_clicked_BM2)
                                                                    endlevel_page_failed.draw(win)
                                                                    score_font = pygame.font.SysFont("name", 50)
                                                                    text_score = score_font.render("score: "+str(score), 1, text_color)
                                                                    win.blit(text_score, (score_display))
                                                                    draw_levelmenu_text()
                                                                    pygame.display.update()
                                                                    menule_notclicked2 = False
                                                                
                                                                                                 
                        
                        
                                    # 4 Entering name (if fails: its same as the above)
                                    if event.type == pygame.KEYDOWN:
                                        pygame.time.delay(15)
                                        if chr(event.key) == "\b":
                                            player_name = player_name[0:-1]
                                            endlevel_page_failed.draw(win)
                                            win.blit(text_score, (score_display))
                                            player_font = pygame.font.SysFont("name", 35)
                                            text_player = player_font.render(player_name, 1, text_color)
                                            win.blit(text_player, name_display)                                        
                                            pygame.display.update()
                                        else:
                                            if len(player_name) < max_name:
                                                player_name += chr(event.key)
                                                player_font = pygame.font.SysFont("name", 35)
                                                text_player = player_font.render(player_name, 1, text_color)
                                                win.blit(text_player, name_display)
                                                pygame.display.update() 
                            
                    
    # start_page.draw(win)
    # pygame.display.update()
    
pygame.quit()




    











