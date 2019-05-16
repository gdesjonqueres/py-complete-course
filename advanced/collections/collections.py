"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""

from collections import Counter

temperatures = [14, 14.5, 15, 14, 15.5, 17.1, 14.5, 13, 21]
temperature_counter = Counter(temperatures)
print(temperature_counter[14.5])


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
print(alma_maters['Jean']) # raise keyerror
