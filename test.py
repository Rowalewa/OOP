class Staff:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def summary(self):
        return f'{self.name} {self.gender} {self.age}'


class Teacher(Staff):
    def __init__(self, name, gender, age, subject):
        super().__init__(name, gender, age)
        self.subject = subject


Teacher1 = Teacher('Harry', 'M', 30, 'English')
print(Teacher1.summary(), Teacher1.subject)