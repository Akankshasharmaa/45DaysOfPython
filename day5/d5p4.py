def make_abba(a, b):
    newstr = a + b + b + a
    if len(a) >= 1 and len(b) >= 1:
        return newstr
    else:
        return False

result = make_abba('Hi', 'Bye')
print(result)
result = make_abba('Yo', 'Alice')
print(result)
result = make_abba('', '')
print(result)