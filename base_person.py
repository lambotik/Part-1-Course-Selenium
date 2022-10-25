class People():
    """Create people"""

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        """default weight meaning for all persons"""
        self.weight = 100

    def description_person(self):
        """Get description person"""
        description = self.name + ' ' + str(self.age) + ' years old' + ', his height is ' + str(
            self.height) + 'cm' + ', his weight is ' + str(self.weight) + 'kg'
        print('New person name is: ' + description)

    def get_weight_person(self):
        """Get weight person"""
        print('Weight person is : ' + str(self.weight))

    def update_weight(self, kg):
        """Change weight person"""
        self.weight = kg


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
        print('New warrior name is: ' + description)
