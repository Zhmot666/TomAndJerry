class Cat:
    def __init__(self, name_cat, color_cat, wight_cat):
        self.color = color_cat
        self.wight = wight_cat
        self.name = name_cat

    @staticmethod
    def say():
        print('Мяу')

    def eat(self, what):
        print(f'Я жрат {what.name}')
        self.wight += 1

    @staticmethod
    def run(self, speed):
        print(f'Кот догоняет со скоростью {speed}')


class Mouse:
    def __init__(self, name_mouse, color_mouse, wight_mouse):
        self.color = color_mouse
        self.wight = wight_mouse
        self.name = name_mouse

    @staticmethod
    def say(self):
        print('Пи-пи-пи')

    @staticmethod
    def run(self, speed):
        print(f'Мышь убегает со скоростью {speed}')


if __name__ == '__main__':
    name_cat = input('Введите имя кота: ')
    name_mouse = input('Введите имя мыши: ')
    Jerry = Cat(name_cat, 'Black & Wight', 4)
    Tom = Mouse(name_mouse, 'Gray', 1)
    Tom.say(Tom)
    Jerry.say()
    Tom.run(Tom, 5)
    Jerry.run(Jerry, 6)
    Jerry.eat(Tom)
    print('Кот теперь весит', Jerry.wight)
