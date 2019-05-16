import json

with open('friends.json', 'r') as file:
    file_contents = json.load(file)  # reads file and turn it into a dictionnary

print(file_contents['friends'][0])


cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'Ford', 'model': 'Focus'}
]

with open('cars.json', 'w') as file:
    json.dump(cars, file)

my_json_string = '[{"name": "Alpha Romeo", "released": 1950}]'

my_car = json.loads(my_json_string)
print(my_car[0]['name'])