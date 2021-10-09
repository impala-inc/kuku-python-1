# x_7_9
#
# 「7-7」のコードに入力から質問と回答を繰り返し登録できるようににコードを追加してください

chatbot = [
    {'question': 'おはよう', 'answer': 'おはようございます'},
    {'question': 'おやすみ', 'answer': 'おやすみなさい'},
    {'question': '今日は何日ですか', 'answer': '2021年11月14日です'},
    {'question': '今日の天気は', 'answer': '雨です'},
    {'question': '何か歌って', 'answer': 'もーもたろさんももたろさん'},
    {'question': 'ジャンケン', 'answer': 'グー'},
]

question = input('質問を登録してください:')
answer = input('質問の回答を登録してください:')

print(chatbot)
