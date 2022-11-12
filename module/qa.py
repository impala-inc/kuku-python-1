def execute(vars, hint, question):
    for i in range(hint):
        ex(f'hint_{i + 1}', vars[f'hint_{i + 1}'])
    for i in range(question):
        qa(f'q_{i + 1}', vars[f'q_{i + 1}'])


def qa(question, value):
    i = 0
    while i < 3:
        answer = input(question + 'の値は:')
        if answer == toStr(value):
            print('正解です')
            print('')
            return
        else:
            i += 1
    print('正解は「' + toStr(value) + '」でした。')
    print('')


def ex(question, value):
    print(question + 'の値は' + toStr(value) + 'です')


def toStr(value):
    value = value.__name__ if type(value) is type else value
    return str(value)
