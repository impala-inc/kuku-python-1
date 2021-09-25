# xx_7_5
#
#

import re

pattern = r'^も.*う$'
str = input('「も」から始まって「う」で終わる言葉を入力してください:')

print(re.match(pattern, str))
