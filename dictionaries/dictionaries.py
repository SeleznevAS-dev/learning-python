# 1.
# import random

# keys = []
# for i in range(100):
#     keys.append(random.randint(1, 100))

# dictionary = {}
# for i in range(len(keys)):
#     index_str = str(i)
#     dictionary[keys[i]] = index_str

# for i in dictionary.keys():
#     print(dictionary[i])

# for key in list(dictionary.keys()):
#     del dictionary[key]

# 2.
import random

arr = []
for i in range(100):
    arr.append(random.randint(1, 10))


def n_values(arr, n):
    dct = {}
    for i in arr:
        if i not in dct:
            dct[i] = 0
        else:
            dct[i] += 1
    ans = []
    for key, value in dct.items():
        if value == n:
            ans.append(key)
    return ans
