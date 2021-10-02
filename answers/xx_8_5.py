# xx_8_5
#
# いまいちな部分を修正してください

def examination(result):
    if result >= 40:
        if result >= 60:
            if result >= 80:
                print('よくできました')
            else:
                print('まずまずです')
        else:
            print('頑張りましょう')
    else:
        print('追試です')


examination(90)
