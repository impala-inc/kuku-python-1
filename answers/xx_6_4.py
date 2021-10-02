# xx_6_4
#
#

def member(index):
    members = ['桃太郎', 'いぬ', 'さる', 'きじ']

    try:
        return members[index]
    except IndexError:
        return 'リストの範囲外です'


print(member(5))
