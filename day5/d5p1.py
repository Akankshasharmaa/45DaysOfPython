def string_match(str1, str2):
    substr1 = []
    substr2 = []

    for i in range(len(str1) - 1):
        substr1.append(str1[i:(i+2)])   
    print(substr1)

    for j in range(len(str2) - 1):
        substr2.append(str2[j:(j+2)])
    print(substr2)

    main_lenght = min_lenght(substr1, substr2)
    
    count = 0
    for i in range(main_lenght):
        if substr1[i] == substr2[i]:
            count = count + 1
    return count

def min_lenght(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    if m < n:
        k = m 
    elif n < m:
        k = n
    else: 
        k = m = n

    return k


result = string_match('aabbccdd', 'abbbxxd')
print(result)
result = string_match('abc', 'abc')
print(result)
result = string_match('aaxxaaxx', 'iaxxai')
print(result)
result = string_match('iaxxai', 'aaxxaaxx')
print(result)