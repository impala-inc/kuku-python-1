# x_9_2
#
# 「9-1」を参考にして、「7-7」の辞書を「files」フォルダにある「chatbot.csv」から読み込むように修正してください

import csv

file = open('./files/chatbot.csv', encoding="utf-8")

chatbot = csv.DictReader(file)

message = input('何か話しかけてください:')

for q_and_a in chatbot:
    if q_and_a['question'] == message:
        print(q_and_a['answer'])
        break

file.close()
