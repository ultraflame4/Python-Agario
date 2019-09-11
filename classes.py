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

class player:
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
    def movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.rect[0] > 0:
            self.rect.move_ip((-(self.width/2)), 0)

        if key[pygame.K_d] and (self.rect[0] + self.width) < 700:
            self.rect.move_ip((self.width/2), 0)

        if key[pygame.K_w] and self.rect[1] > 50:
            self.rect.move_ip(0, (-(self.height/2)))

        if key[pygame.K_s] and (self.rect[1] + self.height) < 700:
            self.rect.move_ip(0, (self.height/2))

    def draw(self):
        self.movement()
        pygame.draw.rect(self.surface, self.color, self.rect)



class dot:
    def __init__(self, surface):
        self.surface = surface
        self.x = random.randint(0, 650)
        self.y = random.randint(50, 650)
        self.width = 10
        self.height = 10
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
