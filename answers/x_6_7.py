# x_6_7
#
# 「while文」を追加して以下のように表示してください
#
# 鬼鬼鬼鬼鬼
# 鬼鬼鬼鬼鬼
# 鬼鬼鬼鬼鬼
# 鬼鬼鬼鬼鬼
# 鬼鬼鬼鬼鬼

gyou = 0
while gyou < 5:
    retu = 0
    text = ''
    while retu < 5:
        text += '鬼'
        retu += 1
    print(text)
    gyou += 1
