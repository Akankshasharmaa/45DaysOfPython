first_list = range(11)
second_list = range(1,12)

ziplist = list(zip(first_list, second_list))

def square(a, b):
    return (a*a) + (b*b) + 2 * a * b

# output = [square(item[0], item[1]) for item in ziplist]
output = [square(a, b) for a, b in ziplist]
print(output)

def square2(pair):
    a = pair[0]
    b = pair[1]
    return (a*a) + (b*b) + 2 * a * b

map_list = list(map(square2, ziplist))
print(map_list)