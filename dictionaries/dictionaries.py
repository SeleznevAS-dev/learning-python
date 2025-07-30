# 1.
import random

keys = []
for i in range(100):
    keys.append(random.randint(1, 100))

dictionary = {}
for i in range(len(keys)):
    index_str = str(i)
    dictionary[keys[i]] = index_str

for i in dictionary.keys():
    print(dictionary[i])

for key in list(dictionary.keys()):
    del dictionary[key]
