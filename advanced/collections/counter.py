from collections import Counter

temperatures = [14, 14.5, 15, 14, 15.5, 17.1, 14.5, 13, 21]
temperature_counter = Counter(temperatures)
print(temperature_counter[14.5])
