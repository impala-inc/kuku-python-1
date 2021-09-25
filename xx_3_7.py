# xx_3_7
#
# 「xx_3_2」の「damaged()」をクラスのメソッド（関数）に追加してください。

class Character:
    def __init__(self, name, hit_points, attack):
        self.name = name
        self.hit_points = hit_points
        self.attack = attack

    def hello(self):
        print('初めまして私の名前は' + self.name + 'です')


momotaro = Character('桃太郎', 1800, 220)


def damaged(character, val):
    character.hit_points -= val
    print(character.name + 'は' + str(int(val)) + 'のダメージを受けた')
    print('残りHPは' + str(character.hit_points))


damaged(momotaro, 200)
