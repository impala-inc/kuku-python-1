# xx_3_3
#
#

class Character:
    def __init__(self, name, hit_points, attack):
        self.name = name
        self.hit_points = hit_points
        self.attack = attack

    def greeting(self):
        print('初めまして私の名前は' + self.name + 'です')


momotaro = Character('桃太郎', 1800, 220)
momotaro.greeting()
