# x_9_2
#
# 「9-1」を参考にして、「7-7」の辞書を「files」フォルダにある「chatbot.csv」から読み込むように修正してください

chatbot = [
    {'question': 'おはよう', 'answer': 'おはようございます'},
    {'question': 'おやすみ', 'answer': 'おやすみなさい'},
    {'question': '今日は何日ですか', 'answer': '2021年11月14日です'},
    {'question': '今日の天気は', 'answer': '雨です'},
    {'question': '何か歌って', 'answer': 'もーもたろさんももたろさん'},
    {'question': 'ジャンケン', 'answer': 'グー'},
]

message = input('何か話しかけてください:')

for q_and_a in chatbot:
    if q_and_a['question'] == message:
        print(q_and_a['answer'])
        break
