import pygame
import colors
from classes import *
import interface
import dot_engine
pygame.init()

screen = pygame.display.set_mode((700, 700))

pygame.display.set_caption('Python Agario')
w = 10
h = 10
x = 10
y = 10
vel = 10

run = True
player = player(screen, colors.azure3, 20, 20, 335, 340)
scoreboard = Score()
dotGroup = dot_engine.all_dot(screen, player.rect)

while run:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False
    screen.fill(colors.azure)

    dotGroup.pos_check(scoreboard)
    dotGroup.draw()
    player.draw()
    interface.gui(screen, scoreboard)
    pygame.display.update()
