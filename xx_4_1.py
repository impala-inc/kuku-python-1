# xx_4_1
#
#

class Dog():
    def speak(self):
        print('ワンワン')


class Monkey():
    def speak(self):
        print('ウッキッキー')


class Pheasant():
    def speak(self):
        print('ケーン')


dog = Dog()
monkey = Monkey()
pheasant = Pheasant()

members = [dog, monkey, pheasant]

for member in members:
    member.speak()
