# x_6_7
#
# 「while文」を使って以下のように表示してください(鬼の真ん中に桃が１文字含まれています)
#
# 鬼鬼鬼鬼鬼
# 鬼鬼鬼鬼鬼
# 鬼鬼桃鬼鬼
# 鬼鬼鬼鬼鬼
# 鬼鬼鬼鬼鬼

gyou = 0
while gyou < 5:
    retu = 0
    text = ''
    while retu < 5:
        if gyou == 2 and retu == 2:
            text += '桃'
        else:
            text += '鬼'
        retu += 1
    print(text)
    gyou += 1
