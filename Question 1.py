fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

filterfruits = list(filter(lambda  x: len(x) > 5, fruits))

print(filterfruits)