def missing_char(myString, n):
    abc = []
    newStr = ''
    for i in range(len(myString)):
        abc.append(myString[i])
    abc.pop(n)
    for j in abc:
        newStr = newStr + j
    return newStr
    
        
result = missing_char('kitten', 1)
print(result)
result = missing_char('kitten', 0)
print(result)
result = missing_char('kitten', 4)
print(result)
result = missing_char('kitten', 5)
print(result)