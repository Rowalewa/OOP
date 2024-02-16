class Calculator:

    @staticmethod
    def sum(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b


c = Calculator()
print(c.sum(9, 5))
print(c.subtract(9, 5))
print(c.multiply(9, 5))
print(c.divide(9, 5))
