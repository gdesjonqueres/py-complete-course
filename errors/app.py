class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a `{car.__class__.__name__}` to the garage but you can only add `Car` object')
        self.cars.append(car)


ford = Garage()
fiesta = Car('Ford', 'Fiesta')

# Python prefers forgiveness over permission, instead of checking beforehand if the parameter is valid
# we let the error happens and catch it
try:
    # ford.add_car(fiesta)
    ford.add_car('fiesta')
except TypeError:
    print('Your car was not a car')
except ValueError:
    print('Something weird happened...')
finally:
    print(f'The garage now has {len(ford)} car(s)')