def execute(vars):
    keys = sorted(list(vars.keys()))

    for key in keys:
        if key.startswith('hint_'):
            ex(key, vars[key])
    for key in keys:
        if key.startswith('q_'):
            qa(key, vars[key])


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
