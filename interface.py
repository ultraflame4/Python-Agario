import pygame
import colors
def gui(surface,score_board, life_counter):
    font = pygame.font.Font("font.ttf", 32)
    Score_text = font.render(('Score : ' + str(score_board.score)), True, colors.azure)
    Lives_text = font.render(('Lifes : ' + str(life_counter.lifes)), True, colors.azure)
    pygame.draw.rect(surface, colors.azure4, (0, 0, 700, 50))
    surface.blit(Score_text, (5, 5))
    surface.blit(Lives_text, (520, 5))

