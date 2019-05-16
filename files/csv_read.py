csv_file = open('csv_data.txt', 'r')
# data = [line.strip() for i, line in enumerate(csv_file.readlines()) if i > 0]
lines = csv_file.readlines()
csv_file.close()

lines = [line.strip() for line in lines[1:]]
for line in lines:
    person_data = line.split(',')
    name = person_data[0].title()
    age = person_data[1]
    university = person_data[2].title()
    degree = person_data[3].capitalize()

    print(f'{name} is studying {degree} at {university}.')

sample_csv_value = ','.join(['Rolf', '25', 'MIT', 'Computer Science'])
print(sample_csv_value)
