# xx_8_1
#
# いまいちな部分を修正してください

weight = 65
height = 1.7

if weight / (height * height) < 18.5:
    print('痩せ')
elif weight / (height * height) < 24.9:
    print('普通')
elif weight / (height * height) < 30.0:
    print('肥満')
else:
    print('高度肥満')
