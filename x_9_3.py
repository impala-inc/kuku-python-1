# x_9_3
#
# 「7-9」で入力した質問と回答を「chatbot.csv」に保存するように修正してください

import csv

file = open('./files/chatbot.csv', mode='a', encoding="utf-8")

labels = ['question', 'answer']
writer = csv.DictWriter(file, fieldnames=labels)
writer.writerow({'question': '山口県の県庁所在地', 'answer': '山口市'})

file.close()
