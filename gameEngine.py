from classes import *
import colors
import pygame
class dotEngine:
    def __init__(self, surface, player_rect):
        self.surface = surface
        self.dots = [dot(self.surface) for i in range(100)]
        self.PlayerRECT = player_rect

    def draw(self):
        for i in self.dots:i.draw()

    def pos_check(self,scoreObj, playerFunc):

        for i in self.dots:
            self.check_collide(i, scoreObj, playerFunc)


    def check_collide(self, the_dot, scoreAdd, player):
        if the_dot.rect.colliderect(self.PlayerRECT):
            the_dot.generate()
            scoreAdd.add(1)
            the_dot.draw()
            player.enlarge()


    def rectUpdate(self, playerRect):
        self.PlayerRECT = playerRect

    def update(self, scoreObj, playerFunc):
        self.pos_check(scoreObj, playerFunc)
        self.draw()

class playerEngine:
    def __init__(self, surface):
        self.Player = playerObj(surface, colors.azure3, 10, 10, 335, 340)
        self.speed=5

    def enlarge(self):
        if self.Player.rect[2] < 25:
            self.Player.rect[2] += 2
            self.Player.rect[3] += 2
        elif self.Player.rect[2] < 65:
            self.Player.rect[2] += 1
            self.Player.rect[3] += 1

    def deEnlarge(self, amount):
        self.Player.rect[2] -= amount
        self.Player.rect[3] -= amount

    def movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.Player.rect[0] > 0:
            self.Player.rect.move_ip(-self.speed, 0)

        if key[pygame.K_d] and (self.Player.rect[0] + self.Player.rect[2]) < 700:
            self.Player.rect.move_ip(self.speed, 0)

        if key[pygame.K_w] and self.Player.rect[1] > 50:
            self.Player.rect.move_ip(0, -self.speed)

        if key[pygame.K_s] and (self.Player.rect[1] + self.Player.rect[3]) < 700:
            self.Player.rect.move_ip(0, self.speed)

    def draw(self):
        self.movement()
        self.Player.draw()

class virusEngine:
    def __init__(self, surface, player,score):
        self.surface = surface
        self.playerInstance = player
        self.score = score
        ###

        self.viruses = [virusDot(surface) for i in range (10)]

    def drawLogic(self, virusObj):
        if self.playerInstance.Player.rect[2] >= virusObj.rect[2]:
            virusObj.draw()
            self.playerInstance.draw()
            return True
        else:
            self.playerInstance.draw()
            virusObj.draw()
            return False
    def draw(self):
        for i in self.viruses:
            self.drawLogic(i)

    def mass_check(self, scoreboard):
        for i in self.viruses:
            self.check_collision(i)

    def check_collision(self, selfVirus):
        if selfVirus.rect.colliderect(self.playerInstance.Player.rect) and self.playerInstance.Player.rect[2]>selfVirus.rect[2]: # check if player is bigger than virus
            if self.drawLogic(selfVirus):
                selfVirus.generate()
                self.playerInstance.deEnlarge(10)

            if self.playerInstance.Player.rect[2] > 15:
                self.playerInstance.deEnlarge(5)

            self.score.add(random.randrange(5, 30))


    def update(self, scoreObj):
        self.mass_check(scoreObj)
        self.draw()
