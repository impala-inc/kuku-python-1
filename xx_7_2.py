# xx_7_2
#
#

import re

pattern = 'い'
str = input('ひらがなの「い」のつく言葉を入力してください:')

print(re.sub(pattern, 'ﾚヽ', str))
