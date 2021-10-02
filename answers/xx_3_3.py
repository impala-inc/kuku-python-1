# xx_3_3
#
# 「scouter()」を「hello()」のようなクラスのインスタンスメソッド（関数）に修正してください。

class Character:
    def __init__(self, name, hit_points, attack):
        self.name = name
        self.hit_points = hit_points
        self.attack = attack

    def hello(self):
        print('初めまして私の名前は' + self.name + 'です')


momotaro = Character('桃太郎', 1800, 220)
momotaro.hello()


def scouter(character):
    print('名前:' + character.name)
    print('HP:' + str(character.hit_points))
    print('攻撃力:' + str(character.attack))


print(scouter(momotaro))
