class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    # @staticmethod
    # def from_sum(value1, value2):
    #     return FixedFloat(value1 + value2)
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

number = FixedFloat(18.5746)
print(number)
another_number = FixedFloat.from_sum(45.5489, 87.6489)
print(another_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = 'EUR'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'


money = Euro(18.786)
print(money)

# si l'on n'avait pas redefini from_sum comme une "classmethod"
# au lieu d'une "staticmethod", on aurait un FixedFloat au lieu d'un Euro
another_money = Euro.from_sum(12.789, 45.4671)
print(another_money)
