def execute(vars):
    keys = sorted(list(vars.keys()))

    for key in keys:
        if key.startswith('hint_'):
            ex(key, vars[key])
    for key in keys:
        if key.startswith('q_'):
            qa(key, vars[key])


def qa(question, value):
    for _ in range(3):
        answer = input(question + 'の値は:')
        if answer == toStr(value):
            print('正解です', end='\n\n')
            return

    print('正解は「', toStr(value), '」でした。', sep='', end='\n\n')


def ex(question, value):
    print(question, 'の値は', toStr(value), 'です', sep='')


def toStr(value):
    value = value.__name__ if type(value) is type else value
    return str(value)
