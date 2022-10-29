# x_8_9
#
# 「cards」を「while文」と「random」を使ってランダムに並び替えてください

import random

cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

print(cards)

count = 0
while count < 20:
    f = random.randint(0, 12)
    t = random.randint(0, 12)

    if f != t:
        cards[f], cards[t] = cards[t], cards[f]  # cards[f]とcards[t]の要素を交換
        count += 1

    print(cards)
