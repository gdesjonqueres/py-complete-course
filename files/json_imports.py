import json

file = open('friends.json', 'r')
file_contents = json.load(file)  # reads file and turn it into a dictionnary
file.close()

print(file_contents['friends'][0])

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

file = open('cars.json', 'w')
json.dump(cars, file)
file.close()

my_json_string = '[{"name": "Alpha Romeo", "released": 1950}]'
my_car = json.loads(my_json_string)
print(my_car[0]['name'])