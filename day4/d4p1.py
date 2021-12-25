def string_bits(mystr):
    newstr = ''
    for i in range(0, len(mystr), 2):
        newstr = newstr + mystr[i]
    return newstr

result = string_bits('Hello')
print(result)
result = string_bits('Hi')
print(result)
result = string_bits('Heeololeo')
print(result)