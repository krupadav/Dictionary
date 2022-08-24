a = {1: 'a', 2: 'b', 3: 'c'}
print(a)
print(a.keys())  # gives key
print(a.values())  # gives values
print(a.items())  # gives items(key-value)
print(a.pop(3))  # in pop we must supply a key to be removed, it removes and return the value.
print(a.popitem())  # it by default removes last key value pair. If dict is empty then we get key error.
print(a.get(2))  # it gives value associated to key and if key is not present then output is None
