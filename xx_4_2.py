# xx_4_2
#
#

kana = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ']
gal_kana = ['ぁ', 'ﾚヽ', 'ぅ', 'ぇ', 'ぉ', 'ｶゝ', '､ｷ', '＜', 'ﾚﾅ', '⊇']

table = dict(zip(kana, gal_kana))

text = 'あおいうみのちかくのこうえん'

print(text.translate(str.maketrans(table)))
