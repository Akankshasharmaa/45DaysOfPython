def string_match(str1, str2):
    substr1 = []
    substr2 = []
    for i in range(len(str1) - 1):
        substr1.append(str1[i:(i+2)])   

    for j in range(len(str2) - 1):
        substr2.append(str2[j: (j+2)])

    counter = 0
    for substr in substr1:
        for substrr in substr2:
            if substr == substrr:
                counter = counter + 1
    return counter
    
result = string_match('xxcaazz', 'xxbaaz')
print(result)
result = string_match('abc', 'abc')
print(result)
result = string_match('', '')
print(result)
