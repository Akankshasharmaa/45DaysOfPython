def last2(str):
    substr = []
    for i in range(len(str) - 1):
        substr.append(str[i: (i+2)])
    
    counter = 0
    for j in range(len(substr) - 1):
        if substr[j] == substr[len(substr) - 1]:
            counter = counter + 1
    return counter

result = last2('hixxhi')
print(result)
result = last2('xaxxaxaxx')
print(result)
result = last2('')
print(result)