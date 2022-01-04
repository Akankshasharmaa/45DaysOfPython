def count_hi(str):
    count = 0

    for i in range(len(str)):
        if str[i] == 'h' and str[i+1] == 'i':
            count += 1
    return count

result = count_hi('abc hi ho')
print(result)
result = count_hi('ABChi hi')
print(result)
result = count_hi('hihi')
print(result)