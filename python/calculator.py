

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
        return a // b

    @staticmethod
    def mod(a, b):
        return a % b


cal = Calculator()

print(cal.subtract(10, 5))

