def qa(question, value):
    i = 0
    while i < 3:
        answer = input(question + 'の値は:')
        if answer == str(value):
            print('正解です')
            print('')
            return
        else:
            i += 1
    print('正解は' + str(value) + 'でした。')
    print('')


def ex(question, value):
    print(question + 'の値は' + str(value) + 'です')
