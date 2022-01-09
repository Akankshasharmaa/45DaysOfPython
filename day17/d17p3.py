import math

x = list(range(10,0, -1))

y = [math.ceil(math.sqrt(item)) for item in x]

ziplist = list(zip(x,y))
print(ziplist)
print([(10, 4), (9, 3), (8, 3), (7, 3), (6, 3), (5, 3), (4, 2), (3, 2), (2, 2), (1, 1)])