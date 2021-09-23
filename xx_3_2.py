# xx_3_2
#
#

class Character:
    def __init__(self, name, hit_points, attack):
        self.name = name
        self.hit_points = hit_points
        self.attack = attack


momotaro = Character('桃太郎', 1800, 220)


def scouter(character):
    print('名前は' + character.name)
    print('HPは' + str(character.hit_points))
    print('攻撃力は' + str(character.attack))


print(scouter(momotaro))
