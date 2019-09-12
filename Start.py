#!venv/Scripts/python
import pygame
import colors
from classes import *
import interface
import gameEngine

pygame.init()

screen = pygame.display.set_mode((700, 700))

pygame.display.set_caption('Python Agario')

run = True
player = gameEngine.playerEngine(screen)
scoreboard = Score()
dotGroup = gameEngine.dotEngine(screen, player.Player.rect)
while run:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False
    screen.fill(colors.azure)

    dotGroup.rectUpdate(player.Player.rect)
    dotGroup.pos_check(scoreboard, player)
    dotGroup.draw()
    player.draw()
    interface.gui(screen, scoreboard)
    pygame.display.update()
