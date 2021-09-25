# xx_7_1
#
#

import re

pattern = 'ももたろう'

print(re.search(pattern, 'ももたろう'))
print(re.match(pattern, 'ももたろう'))
print(re.fullmatch(pattern, 'ももたろう'))

print(re.search(pattern, 'ももたろう侍'))
print(re.match(pattern, 'ももたろう侍'))
print(re.fullmatch(pattern, 'ももたろう侍'))

print(re.search(pattern, '桃から生まれたももたろう'))
print(re.match(pattern, '桃から生まれたももたろう'))
print(re.fullmatch(pattern, '桃から生まれたももたろう'))

print(re.search(pattern, '桃から生まれたももたろう侍'))
print(re.match(pattern, '桃から生まれたももたろう侍'))
print(re.fullmatch(pattern, '桃から生まれたももたろう侍'))
