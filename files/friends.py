# Ask for a list of three friends
# For each, we'll tell the user if they are nearby
# for each nearby friend, we'll save their name to the `nearby_friends.txt`

# friends_input = input('Please enter a list of 3 three friends separated by `,`: ')
# friends_input = friends_input.strip()
# friends_list = friends_input.split(',')
#
# # people_list = []
# people_file = open('people.txt', 'r')
# people_list = people_file.readlines()
# people_file.close()
#
# nearby_friends_list = []
# for friend in friends_list:
#     if friend.lower() in [person.lower().strip(' \n') for person in people_list]:
#         nearby_friends_list.append(friend)
#         print(f'{friend} is nearby')
#
# nearby_friends_file = open('nearby_friends.txt', 'w')
# nearby_friends_file.writelines(nearby_friends_list)
# nearby_friends_file.close()


friends = input('Enter three friends name separated by `comma`, no space between them: ').split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]
people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = people_nearby_set.intersection(friends_set)

nearby_friends_file = open('nearby_friends.txt', 'w')
for friend in friends_nearby_set:
    print(f'{friend} is nearby')
    nearby_friends_file.write(f'{friend}\n')
nearby_friends_file.close()
