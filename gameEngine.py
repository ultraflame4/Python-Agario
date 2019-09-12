from classes import dot, playerObj
import colors
import pygame
class dotEngine:
    def __init__(self, surface, player_rect):
        self.surface = surface
        self.dot1 = dot(self.surface)
        self.dot2 = dot(self.surface)
        self.dot3 = dot(self.surface)
        self.dot4 = dot(self.surface)
        self.dot5 = dot(self.surface)
        self.dot6 = dot(self.surface)
        self.dot7 = dot(self.surface)
        self.dot8 = dot(self.surface)
        self.dot9 = dot(self.surface)
        self.dot10 = dot(self.surface)
        self.dot11 = dot(self.surface)
        self.dot12 = dot(self.surface)
        self.dot13 = dot(self.surface)
        self.dot14 = dot(self.surface)
        self.dot15 = dot(self.surface)
        self.dot16 = dot(self.surface)
        self.dot17 = dot(self.surface)
        self.dot18 = dot(self.surface)
        self.dot19 = dot(self.surface)
        self.dot20 = dot(self.surface)
        self.PlayerRECT = player_rect

    def draw(self):
        self.dot1.draw()
        self.dot2.draw()
        self.dot3.draw()
        self.dot4.draw()
        self.dot5.draw()
        self.dot6.draw()
        self.dot7.draw()
        self.dot8.draw()
        self.dot9.draw()
        self.dot10.draw()
        self.dot11.draw()
        self.dot12.draw()
        self.dot13.draw()
        self.dot14.draw()
        self.dot15.draw()
        self.dot16.draw()
        self.dot17.draw()
        self.dot18.draw()
        self.dot19.draw()
        self.dot20.draw()

    def pos_check(self,scoreObj, playerFunc):
        self.check_engine(self.dot1, scoreObj, playerFunc)
        self.check_engine(self.dot2, scoreObj, playerFunc)
        self.check_engine(self.dot3, scoreObj, playerFunc)
        self.check_engine(self.dot4, scoreObj, playerFunc)
        self.check_engine(self.dot5, scoreObj, playerFunc)
        self.check_engine(self.dot6, scoreObj, playerFunc)
        self.check_engine(self.dot7, scoreObj, playerFunc)
        self.check_engine(self.dot8, scoreObj, playerFunc)
        self.check_engine(self.dot9, scoreObj, playerFunc)
        self.check_engine(self.dot10, scoreObj, playerFunc)
        self.check_engine(self.dot11, scoreObj, playerFunc)
        self.check_engine(self.dot12, scoreObj, playerFunc)
        self.check_engine(self.dot13, scoreObj, playerFunc)
        self.check_engine(self.dot14, scoreObj, playerFunc)
        self.check_engine(self.dot15, scoreObj, playerFunc)
        self.check_engine(self.dot16, scoreObj, playerFunc)
        self.check_engine(self.dot17, scoreObj, playerFunc)
        self.check_engine(self.dot18, scoreObj, playerFunc)
        self.check_engine(self.dot19, scoreObj, playerFunc)
        self.check_engine(self.dot20, scoreObj, playerFunc)

    def check_engine(self, the_dot, scoreAdd, player):
        if the_dot.rect.colliderect(self.PlayerRECT):
            the_dot.generate()
            scoreAdd.add(1)
            the_dot.draw()
            player.enlarge()


    def rectUpdate(self, playerRect):
        self.PlayerRECT = playerRect

class playerEngine:
    def __init__(self, surface):
        self.Player = playerObj(surface, colors.azure3, 10, 10, 335, 340)

    def enlarge(self):
        if self.Player.rect[2] != 50:
            self.Player.rect[2] += 1
            self.Player.rect[3] += 1

    def movement(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a] and self.Player.rect[0] > 0:
            self.Player.rect.move_ip((-(self.Player.rect[3]/2)), 0)

        if key[pygame.K_d] and (self.Player.rect[0] + self.Player.rect[2]) < 700:
            self.Player.rect.move_ip((self.Player.rect[3]/2), 0)

        if key[pygame.K_w] and self.Player.rect[1] > 50:
            self.Player.rect.move_ip(0, (-(self.Player.rect[2]/2)))

        if key[pygame.K_s] and (self.Player.rect[1] + self.Player.rect[3]) < 700:
            self.Player.rect.move_ip(0, (self.Player.rect[2]/2))

    def draw(self):
        self.movement()
        self.Player.draw()
