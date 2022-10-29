# x_1_6
#
# ヒントを参考にq_1 ~ q_4がそれぞれどんな値となるかを予想してください
from module.qa import qa, ex

# ヒント

hint_1 = len('ももたろう')
hint_2 = len('いぬ')
hint_3 = len('あかおに')

# ここから問題

q_1 = len('オムライス')
q_2 = len('カレー')
q_3 = len('ペペロンチーノ')
q_4 = len('ビーフストロガノフ')


# ここはとりあえず無視

for i in range(3):
    ex(f'hint_{i + 1}', locals()[f'hint_{i + 1}'])
for i in range(4):
    qa(f'q_{i + 1}', locals()[f'q_{i + 1}'])
