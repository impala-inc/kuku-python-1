# x_9_6
#
# チャットボットに何か話しかけて同じ質問の答えが複数あれば答えをランダムで返すように修正してください

import random

chatbot = [
    {'question': 'おはよう', 'answer': 'おはようございます'},
    {'question': 'おやすみ', 'answer': 'おやすみなさい'},
    {'question': '今日は何日ですか', 'answer': '2021年11月14日です'},
    {'question': '今日の天気は', 'answer': '雨です'},
    {'question': '今日の天気は', 'answer': '晴れです'},
    {'question': '今日の天気は', 'answer': '曇りです'},
    {'question': '今日の天気は', 'answer': '雪です'},
    {'question': '何か歌って', 'answer': 'もーもたろさんももたろさん'},
    {'question': 'ジャンケン', 'answer': 'グー'},
]

conversation = input('何か話しかけてください:')

answers = []

for q_and_a in chatbot:
    if q_and_a['question'] == conversation:
        answers.append(q_and_a['answer'])

print(random.choice(answers))
