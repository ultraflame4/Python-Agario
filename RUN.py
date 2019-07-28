import pygame
import random
from time import sleep
#
#The Real Shit
pygame.init()
screen = pygame.display.set_mode((800, 900))
pygame.display.set_caption('Blocky Getty Dotty')
pygame.font.init()
text = pygame.font.SysFont('Comfortaa Light', 70)
lifes_symbol = pygame.transform.scale(pygame.image.load('resources\heart.png'), (70, 70))
controls_image = pygame.image.load('resources\CONTROLS.png')
pause_image = pygame.image.load('resources\Pause.png')
lifes = 3
run = True
Score = 0
white = (255, 255, 255)

block_y = 500
block_x = 400
direction = 0
vel = 1
black = (0, 0, 0)
game_speed = 25
dot_spawn = True
dot_spawn2 = True
dot_spawn3 = True
dot_spawn4 = True
dot_spawn5 = True
dot_spawn6 = True
dot_spawn7 = True
dot_spawn8 = True
dot_spawn9 = True
dot_spawn10 = True
Start_menu = True
Pause = False
direction_m = 0
val = 0

cheat = True

try:
    with open('cheat/lives.cheat', 'r'):
        pass
    with open('cheat/speed.cheat', 'r'):
        pass
    with open('cheat/score.cheat', 'r'):
        pass
except FileNotFoundError:
    cheat = False
while run:
    #CHEATS
    if cheat:
        #life
        f = open('cheat/lives.cheat', 'r')
        cheatlife = int(f.read())
        f.close()
        if cheatlife != -1 or cheatlife < -1:
            lifes = cheatlife
            f = open('cheat/lives.cheat', 'w')
            f.write('-1')
            f.close()
            f = open('cheat/lives.cheat', 'r')
            cheatlife = f.read()
            f.close()
        #Speed
        f = open('cheat/speed.cheat', 'r')
        cheatspeed = int(f.read())
        f.close()
        if cheatspeed != -1 or cheatspeed < -1:
            vel = cheatspeed
            f = open('cheat/speed.cheat', 'w')
            f.write('-1')
            f.close()
            f = open('cheat/speed.cheat', 'r')
            cheatlife = f.read()
            f.close()
        #Score
        f = open('cheat/score.cheat', 'r')
        cheatScoreAdd = int(f.read())
        f.close()
        if cheatScoreAdd != 0:
            Score += cheatScoreAdd
            f = open('cheat/score.cheat', 'w')
            f.write('0')
            f.close()


    #INPUIT
    keys = pygame.key.get_pressed()
    #Exit / Pause ? Continue shit===============================================================
    #Exit
    pygame.time.delay(game_speed)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Pause
    if keys[pygame.K_p]:

        if direction_m == 0:
            direction_m = direction
        else:
            direction = 0
        print(direction_m)
        Pause = True
        pygame.display.update()
    if keys[pygame.K_c]:
        if direction == 0:
            direction = direction_m
        else:
            direction_m = 0
        game_speed = 25
        Pause = False
    if Pause:

        screen.blit(pause_image, (0, 100))
        pygame.display.update()
    #


    #----------------------------------------------
    #DISPLAY
    #Start
    #Menu
    if Start_menu == True:
        screen.blit(controls_image, (0, 0))

        pygame.display.update()
    if keys[pygame.K_SPACE]:
        Start_menu = False
    if Start_menu == False and Pause == False:
        pygame.draw.line(screen, white, (0, 100), (800, 100), 5)

        pygame.draw.line(screen, white, (500, 0), (500, 100), 5)

        screen.blit(lifes_symbol, (650, 10))

        screen.blit(text.render((str(lifes) + '  X'), False, white), (550, 25))

        screen.blit(text.render(('Score:  ' + str(Score)), False, white), (10, 25))

        #player--
        pygame.draw.rect(screen, white, (block_x, block_y, 10, 10))

        pygame.display.update()

        screen.fill(black)

        #Dots
        if dot_spawn == False:
            pygame.draw.rect(screen, dot_color, (dot_x, dot_y, 7, 7))
        if dot_spawn2 == False:
            pygame.draw.rect(screen, dot_color2, (dot_x2, dot_y2, 7, 7))
        if dot_spawn3 == False:
            pygame.draw.rect(screen, dot_color3, (dot_x3, dot_y3, 7, 7))
        if dot_spawn4 == False:
            pygame.draw.rect(screen, dot_color4, (dot_x4, dot_y4, 7, 7))
        if dot_spawn5 == False:
            pygame.draw.rect(screen, dot_color5, (dot_x5, dot_y5, 7, 7))
        if dot_spawn6 == False:
            pygame.draw.rect(screen, dot_color6, (dot_x6, dot_y6, 7, 7))
        if dot_spawn7 == False:
            pygame.draw.rect(screen, dot_color7, (dot_x7, dot_y7, 7, 7))
        if dot_spawn8 == False:
            pygame.draw.rect(screen, dot_color8, (dot_x8, dot_y8, 7, 7))
        if dot_spawn9 == False:
            pygame.draw.rect(screen, dot_color9, (dot_x9, dot_y9, 7, 7))
        if dot_spawn10 == False:
            pygame.draw.rect(screen, dot_color10, (dot_x10, dot_y10, 7, 7))
        #death--------------------------------
        if block_y < 104 or block_y == 890:
            direction = 0
            block_y = 500
            block_x = 400
            lifes -= 1
            dot_spawn = True
            dot_spawn2 = True
            dot_spawn3 = True
            dot_spawn4 = True
            dot_spawn5 = True
            dot_spawn6 = True
            dot_spawn7 = True
            dot_spawn8 = True
            dot_spawn9 = True
            dot_spawn10 = True
        if block_x == 0 or block_x == 790:
            direction = 0
            block_y = 500
            block_x = 400
            dot_spawn = True
            dot_spawn2 = True
            dot_spawn3 = True
            dot_spawn4 = True
            dot_spawn5 = True
            dot_spawn6 = True
            dot_spawn7 = True
            dot_spawn8 = True
            dot_spawn9 = True
            dot_spawn10 = True
            lifes -= 1
        if lifes == 0:
            Score = 0
            lifes = 3
            dot_spawn = True
            dot_spawn2 = True
            dot_spawn3 = True
            dot_spawn4 = True
            dot_spawn5 = True
            dot_spawn6 = True
            dot_spawn7 = True
            dot_spawn8 = True
            dot_spawn9 = True
            dot_spawn10 = True
        #----------Movements----------------------------
        #1-LEFT   2- Right    3- Up    4-Down   CTRL / q - speed up
        keys = pygame.key.get_pressed()

        # SPEED
        if keys[pygame.K_q] or keys[pygame.K_RCTRL] or keys[pygame.K_SPACE] or keys[pygame.K_LSHIFT]:
            game_speed = 0

        else:
            game_speed = 3

    #UP DOWn Left Right
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            direction = 1
        elif keys[pygame.K_RIGHT]or keys[pygame.K_d]:
            direction = 2
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            direction = 3
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            direction = 4

        if direction == 1:
            block_x -= vel
        elif direction == 2:
            block_x += vel
        elif direction == 3:
            block_y -= vel
        elif direction == 4:
            block_y += vel


    #----------------points-------------------------
    #Dots Spawn:
        if dot_spawn == True:
            dot_x = random.randint(10, 780)
            dot_y = random.randint(114, 880)
            dot_color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn = False
        if block_x <= dot_x and (block_x + 10) >= dot_x:
            if block_y <= dot_y and (block_y + 10) >= dot_y:
                Score += 1
                dot_spawn = True
    #dot 2
        if dot_spawn2 == True:
            dot_x2 = random.randint(10, 780)
            dot_y2 = random.randint(114, 880)
            dot_color2 = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn2 = False
        if block_x <= dot_x2 and (block_x + 10) >= dot_x2:
            if block_y <= dot_y2 and (block_y + 10) >= dot_y2:
                Score += 1
                dot_spawn2 = True
    #dot 3
        if dot_spawn3 == True:
            dot_x3 = random.randint(10, 780)
            dot_y3 = random.randint(114, 880)
            dot_color3 = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn3 = False
        if block_x <= dot_x3 and (block_x + 10) >= dot_x3:
            if block_y <= dot_y3 and (block_y + 10) >= dot_y3:
                Score += 1
                dot_spawn3 = True
    #dot4
        if dot_spawn4 == True:
            dot_x4 = random.randint(10, 780)
            dot_y4 = random.randint(114, 880)
            dot_color4 = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn4 = False
        if block_x <= dot_x4 and (block_x + 10) >= dot_x4:
            if block_y <= dot_y4 and (block_y + 10) >= dot_y4:
                Score += 1
                dot_spawn4 = True
    #dot5
        if dot_spawn5 == True:
            dot_x5 = random.randint(10, 780)
            dot_y5 = random.randint(114, 880)
            dot_color5 = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn5 = False
        if block_x <= dot_x5 and (block_x + 10) >= dot_x5:
            if block_y <= dot_y5 and (block_y + 10) >= dot_y5:
                Score += 1
                dot_spawn5 = True
    #dot6
        if dot_spawn6 == True:
            dot_x6 = random.randint(10, 780)
            dot_y6 = random.randint(114, 880)
            dot_color6 = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn6 = False
        if block_x <= dot_x6 and (block_x + 10) >= dot_x6:
            if block_y <= dot_y6 and (block_y + 10) >= dot_y6:
                Score += 1
                dot_spawn6 = True
    #dot 7
        if dot_spawn7 == True:
            dot_x7 = random.randint(10, 780)
            dot_y7 = random.randint(114, 880)
            dot_color7 = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn7 = False
        if block_x <= dot_x7 and (block_x + 10) >= dot_x7:
            if block_y <= dot_y7 and (block_y + 10) >= dot_y7:
                Score += 1
                dot_spawn7 = True

    #dot 8
        if dot_spawn8 == True:
            dot_x8 = random.randint(10, 780)
            dot_y8 = random.randint(114, 880)
            dot_color8 = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn8 = False
        if block_x <= dot_x8 and (block_x + 10) >= dot_x8:
            if block_y <= dot_y8 and (block_y + 10) >= dot_y8:
                Score += 1
                dot_spawn8 = True
    #dot 9
        if dot_spawn9 == True:
            dot_x9 = random.randint(10, 780)
            dot_y9 = random.randint(114, 880)
            dot_color9 = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn9 = False
        if block_x <= dot_x9 and (block_x + 10) >= dot_x9:
            if block_y <= dot_y9 and (block_y + 10) >= dot_y9:
                Score += 1
                dot_spawn9 = True
    #dot10
        if dot_spawn10 == True:
            dot_x10 = random.randint(10, 780)
            dot_y10 = random.randint(114, 880)
            dot_color10 = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
            dot_spawn10 = False
        if block_x <= dot_x10 and (block_x + 10) >= dot_x10:
            if block_y <= dot_y9 and (block_y + 10) >= dot_y10:
                Score += 1
                dot_spawn10 = True

