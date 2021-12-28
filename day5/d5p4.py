def make_abba(a, b):
    newstr = a + b + b + a
    if len(a) >= 0 and len(b) >= 0:
        return newstr
    else:
        return False

result = make_abba('Hi', 'Bye')
print(result)
result = make_abba('Yo', 'Alice')
print(result)
result = make_abba('x', '')
print(result)