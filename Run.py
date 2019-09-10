import pygame
import colors
from classes import *
import interface
pygame.init()
#screen size
screen = pygame.display.set_mode((700, 700))
#sets title of game in the screendow
pygame.display.set_caption('Python Agario')
w = 10
h = 10
x = 10
y = 10
vel = 10

run = True
player = player(screen, colors.azure3, 40, 40, 335, 340)
scoreboard = Score()
lifecounter = lives()
while run:
    pygame.time.delay(60)
    #checks for mouse clicks , keyboard presses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False

    #blank
    screen.fill(colors.azure)
    #draw
    player.draw()
    interface.gui(screen,scoreboard, lifecounter)
    pygame.display.update()
