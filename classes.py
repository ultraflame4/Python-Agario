import pygame
import random
import colors
class Score:
    def __init__(self,scoreINT=0):
        self.score = int(scoreINT)

    def add(self, number):

        self.score += number

    def subtract(self, number):

        self.score -= number

    def set(self, score):

        self.score = score

class playerObj:
    def __init__(self,surface,color,w=10,h=10,x=10,y=10):
        self.surface = surface
        self.color = color
        self.width = w
        self.height = h
        self.X = x
        self.Y = y
        self.rect = pygame.rect.Rect((self.X, self.Y, self.width, self.height))
        self.player = pygame.draw.rect(self.surface, self.color, self.rect)
        self.surfaceSize = pygame.display.get_surface()

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)



class dot:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(0, 650)
        self.y = random.randint(50, 650)
        self.width = 5
        self.height = 5
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
    def draw(self):
        pygame.draw.rect(self.surface, random.choice(colors.basic), self.rect)
    def generate(self):
        self.x = random.randint(0, 650)
        self.y = random.randint(50, 650)
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
class lives:
    def __init__(self, livesINT=0):
        self.lifes = livesINT

    def add(self, number):

        self.lifes += number

    def subtract(self, number):

        self.lifes -= number

    def set(self, setLifes):
        self.lifes = setLifes
