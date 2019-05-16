"""
defaultdict never returns a key error
instead returns a default value
"""

coworkers = [('Rolf', 'MIT'), ('Jen', 'Oxford'), ('Rolf', 'Cambridge'),
    ('Charlie', 'Manchester')]

alma_maters = {}
for coworker, place in coworkers:
    if coworker not in alma_maters:
        alma_maters[coworker] = []
    alma_maters[coworker].append(place)

print(alma_maters)


# instead of this boilerplate we could use a defaultdict and we wouldn't need
# to iniatilize the list of places anymore
from collections import defaultdict

alma_maters = defaultdict(list)  # default value: list (-> [])
for coworker, place in coworkers:
    alma_maters[coworker].append(place)

print(alma_maters)
print(alma_maters['Anna'])  # Anna doesn't exist, default dict returns the default value, in this case []
print(alma_maters)
# it's possible to change the default factory to for example still raise an error in this case
alma_maters.default_factory = None
# print(alma_maters['Jean']) # now raises a keyerror


my_company = 'Teclado'

coworkers = ['Jen', 'Li', 'Charlie', 'Rhys']
other_coworkers = [('Rolf', 'Apple Inc.'), ('Anna', 'Google')]

coworker_companies = defaultdict(lambda: my_company)  # as to be a function

for person, company in other_coworkers:
    coworker_companies[person] = company

print(coworker_companies[coworker[0]])  # Jen doesn't exist so return the default 'Teclado'
print(coworker_companies['Rolf'])
