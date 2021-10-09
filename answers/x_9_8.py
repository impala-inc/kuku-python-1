# x_9_8
#
# 「8-4」を参考にチャットボットを「今何時」という質問に「○○時○○分です」と現在時刻を回答できるように修正してください
# ヒント: 時間と分は「now.hour」と「now.minute」を使います

import datetime

chatbot = {
    'おはよう': 'おはようございます',
    'おやすみ': 'おやすみなさい',
    '今日は何日ですか': '2021年11月14日です',
    '今日の天気は': '雨です',
    '何か歌って': 'もーもたろさんももたろさん',
}

conversation = input('何か話しかけてください:')

if conversation == '今何時':
    now = datetime.datetime.now()
    print(str(now.hour) + '時' + str(now.minute) + '分です')
elif conversation in chatbot:
    print(chatbot[conversation])
else:
    print('わかりません')
