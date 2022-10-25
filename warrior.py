from base_person import People


class Warrior(People):
    """Create class warrior"""

    def __init__(self, name, age, height):
        """Get attribute of parent class"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        print('Conan rage equal ' + str(self.rage))

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ' ' + str(self.age) + ' years old ' + ' and his charge of rage equal ' + str(
            self.rage)
        print('New warrior name is ' + description)


# dima = People('Dima', 34, 172)
# dima.description_person()
# """get default weight person"""
# dima.get_weight_person()
# """change weight person"""
# dima.update_weight(65)
# """get update weight person"""
# dima.get_weight_person()

conan = Warrior('Conan', 30, 120)
# conan.get_weight_person()
# conan.get_rage()
conan.description_person()
