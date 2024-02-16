class Employee:
    def __init__(self, firstname, lastname, age, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.salary = salary

    def summary(self):
        return f'{self.firstname} {self.lastname}, {self.age}, {self.salary}'


class Student:
    def __init__(self, firstname, lastname, code, age, house):
        self.firstname = firstname
        self.lastname = lastname
        self.code = code
        self.house = house
        self.age = age

    def info(self):
        return f'{self.firstname} {self.lastname}, No:{self.code}, age:{self.age}, Hse:{self.house}'


class Person(Employee):
    def __init__(self, firstname, lastname, age, salary, employer):
        super().__init__(firstname, lastname, age, salary)
        self.employer = employer


emp1 = Person('Tom', 'Smith', 20, '20000', 'tsc')
print(emp1.summary(), emp1.employer)


class Person(Student):
    def __init__(self, firstname, lastname, code, age, house, subject):
        super().__init__(firstname, lastname, code, age, house)
        self.subject = subject


s1 = Person("Tom", "Smith", 13901, 18, "Francis", "Engineering")
print(s1.info(), s1.subject)
