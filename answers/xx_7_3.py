# xx_7_3
#
#

import re

pattern = 'い'
str = input('ひらがなの「い」のつく言葉を入力してください:')

print(re.split(pattern, str))
