# xx_3_2
#
# 例にならって「Character」から「いぬ(HP:1300, 攻撃力:180)」と「さる(HP:1400, 攻撃力:150)」と「きじ(HP:1100, 攻撃力:130)」のHPを表示する行を追加してください。

class Character:
    def __init__(self, name, hit_points, attack):
        self.name = name
        self.hit_points = hit_points
        self.attack = attack


momotaro = Character('桃太郎', 1800, 230)


def scouter(character):
    print('名前:' + character.name)
    print('HP:' + str(character.hit_points))
    print('攻撃力:' + str(character.attack))


scouter(momotaro)
