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
        print('New person name : ' + description)

    def get_weight_person(self):
        """Get weight person"""
        print('Weight person is : ' + str(self.weight))

    def update_weight(self, kg):
        """Change weight person"""
        self.weight = kg


dima = People('Dima', 34, 172)
dima.description_person()
"""get default weight person"""
dima.get_weight_person()
"""change weight person"""
dima.update_weight(65)
"""get update weight person"""
dima.get_weight_person()
