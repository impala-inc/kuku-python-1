# x_9_9
#
# 「prefecture.csv」を利用して都道府県番号を答える機能をチャットボットに追加してください

import csv

chatbot = {
    'おはよう': 'おはようございます',
    'おやすみ': 'おやすみなさい',
    '今日は何日ですか': '2021年11月14日です',
    '今日の天気は': '雨です',
    '何か歌って': 'もーもたろさんももたろさん',
}

conversation = input('何か話しかけてください:')

if conversation == '都道府県番号を教えて':
    prefecture = input('何県の都道府県番号ですか？:')

    file = open('./files/prefecture.csv')

    reader = csv.DictReader(file)
    for row in reader:
        if row['都道府県名'] == prefecture:
            print(prefecture + 'の都道府県番号は' + str(row['都道府県番号']) + 'です')
            break

    file.close()
elif conversation in chatbot:
    print(chatbot[conversation])
else:
    print('わかりません')
