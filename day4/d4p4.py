def string_splosion(str):
    newstr = ''
    for i in range(len(str) + 1):
        newstr = newstr + str[:i]
    return newstr

result = string_splosion('Code')
print(result) #'CCoCodCode'
result = string_splosion('abc')
print(result) #'aababc'
result = string_splosion('ab')
print(result)
