
from classes import *
import gameEngine
import interface

pygame.init()

screen = pygame.display.set_mode((700, 700))

pygame.display.set_caption('Python Agario')
pygame.display.set_icon(pygame.image.load("python-Agario.png"))
run = True
player = gameEngine.playerEngine(screen)
scoreboard = Score()
dotGroup = gameEngine.dotEngine(screen, player.Player.rect)
viruses = gameEngine.virusEngine(screen, player,scoreboard)



while run:
    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              run = False

    #Graphics

    interface.draw(screen, player, scoreboard, dotGroup, viruses)
