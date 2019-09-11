from classes import dot
class all_dot:
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

    def pos_check(self,scoreObj):
        self.check_engine(self.dot1, scoreObj)
        self.check_engine(self.dot2, scoreObj)
        self.check_engine(self.dot3, scoreObj)
        self.check_engine(self.dot4, scoreObj)
        self.check_engine(self.dot5, scoreObj)
        self.check_engine(self.dot6, scoreObj)
        self.check_engine(self.dot7, scoreObj)
        self.check_engine(self.dot8, scoreObj)
        self.check_engine(self.dot9, scoreObj)
        self.check_engine(self.dot10, scoreObj)
    def check_engine(self, the_dot, scoreAdd):
        if the_dot.rect.colliderect(self.PlayerRECT):
            the_dot.generate()
            scoreAdd.add(1)
            the_dot.draw()
            return
            pass