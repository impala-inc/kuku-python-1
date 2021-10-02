# xx_7_6
#
#

import re

pattern = r'[山平岡中川本戸井江小木曽]田'
str = input('「田」がつく２文字の苗字を入力してください:')

print(re.match(pattern, str))
