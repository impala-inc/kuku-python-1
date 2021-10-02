# xx_7_4
#
#

import re

pattern = r'\d\d\d-\d\d\d\d'
str = input('郵便番号を入力してください(xxx-xxxx):')

print(re.search(pattern, str))
print(re.match(pattern, str))
print(re.fullmatch(pattern, str))
