set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print(set_one, set_two)

print(set_one.intersection(set_two))
print(set_one & set_two)
print(set_one.union(set_two))
print(set_one | set_two)
print(set_one.difference(set_two))
print(set_one - set_two)

a = [1, 2, 3]
a.append(4)
print(a)

# un tuple est non mutable
b = (1,)
c = b + (2, 3)
print(c)

# chaque element est unique dans un set, pas de garantie d'ordre
d = {'toto', 'titi', 'tata'}
# print(d[0]) => error on ne peut acceder par un index
d.add('tyty')
d.add('tutu')
d.add('tutu')
d.add('tutu')
print(d)
