import pygame
import colors
import gameEngine
def gui(surface,score_board, player):
    font = pygame.font.Font("font.ttf", 32)
    Score_text = font.render(('Score : ' + str(score_board.score)), True, colors.azure)
    Size_textx = font.render(('Player Size : ' + str(player.Player.rect[2])), True, colors.azure)
    pygame.draw.rect(surface, colors.azure4, (0, 0, 700, 50))
    surface.blit(Score_text, (5, 5))
    surface.blit(Size_textx, (400, 5))

def draw(surface, player, scoreboard, dotGroup, viruses):
    surface.fill(colors.azure)
    dotGroup.rectUpdate(player.Player.rect)
    dotGroup.update(scoreboard, player)
    viruses.update()
    gui(surface, scoreboard, player)
    pygame.display.update()
