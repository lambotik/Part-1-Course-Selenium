class Person():
    """Model person"""

    def __init__(self, name, age):
        """Инициализация человека"""
        self.name = name
        self.age = age
        print('Персонаж создан')

    def sing(self):
        """Просим человека спеть"""
        print(self.name + ' Поёт')

    def dance(self):
        """Просим человека станцевать"""
        print(self.name + ' Танцует')


man = Person('Dima', 34)
woman = Person('Sveta', 33)

man.dance()
woman.sing()
