class Bad_pin:
    def __init__(self, pin):
        self.pin = pin
        pin = []


class FourDigitList:
    def __init__(self, digits):
        self.digits = digits

    def iterate(self):
        for digit in self.digits:
            print(digit)


class MultiDigitList:
    def __init__(self):
        self.digits = []

    def add_digits(self, digits):
        self.digits.append(digits)

    def get_digits(self, index):
        return self.digits[index]

