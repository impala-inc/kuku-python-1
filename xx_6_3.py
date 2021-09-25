# xx_6_3
#
#

class MemberError(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message


member = '青鬼'

if member not in ['桃太郎', 'いぬ', 'さる', 'きじ']:
    raise MemberError('foo', 'メンバー以外が紛れ込んでいます。')
