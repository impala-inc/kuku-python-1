# x_8_5
#
# スタートからの経過時間を表示するストップウオッチを作ってください

import datetime

start = datetime.datetime.now()
print('スタート:' + str(start))

input('止める(リターンキーを押してください):')

end = datetime.datetime.now()

print(end - start)
