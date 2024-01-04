class Cat:
    def __init__(self, name_cat, color_cat, wight_cat):
        self.color = color_cat
        self.wight = wight_cat
        self.name = name_cat

    @staticmethod
    def say():
        print('Мяу')

    def eat(self, what):
        print(f'{name_cat} кричит: Я жрат {what.name}')
        self.wight += wight2_mouse

    @staticmethod
    def run(speed):
        print(f'Кот догоняет со скоростью {speed}')


class Mouse:
    def __init__(self, name_mouse, color_mouse, wight_mouse):
        self.color = color_mouse
        self.wight = wight_mouse
        self.name = name_mouse

    @staticmethod
    def say():
        print('Пи-пи-пи')

    @staticmethod
    def run(speed):
        print(f'Мышь убегает со скоростью {speed}')


class Dog:
    def __init__(self, name_dog, color_dog, wight_dog):
        self.color = color_dog
        self.wight = wight_dog
        self.name = name_dog

    @staticmethod
    def say():
        print('Гав,Гав!!!Кот, если ты сьешь мышь, я тебя догоню и сьем!!!!!')

    @staticmethod
    def run(speed):
        print(f'Собака догоняет кота со скоростью {speed}')

    def eat(self, what):
        print(f'Собачка говорит: Упс, ням, я же предупреждал тебя, Кот! {what.name}!')
        self.wight += wight1_cat
        self.wight += wight2_mouse


if __name__ == '__main__':
    name_cat = input('Введите имя кота: ')
    name_mouse = input('Введите имя мыши: ')
    name_dog = input('Введите имя собачки: ')
    wight1_cat = int(input('Введите вес кота: '))
    wight2_mouse = int(input('Введите вес мыши: '))
    wight3_dog = int(input('Введите вес собачки: '))
    Tom = Cat(name_cat, 'Black & Wight', 5)
    Jerry = Mouse(name_mouse, 'Gray', 2)
    Pluto = Dog(name_mouse, 'white', 8)

    Tom.say()
    Jerry.say()
    Pluto.say()
    Tom.run(5)
    Jerry.run(6)
    Pluto.run(10)
    Tom.eat(Jerry)
    Pluto.eat(Tom)
    print(f'Собачка теперь весит {Pluto.wight})))')
    print(f'Котик бы весил {Tom.wight} (((')
    print(f'Вот и сказочки конец, а кто слушал МОЛОДЕЦ!!!!!')
