def count_code(str):
    count = 0
    for i in range(len(str)):
        if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
            count += 1
    return count

result = count_code('aaacodebbb')
print(result)
result = count_code('codexxcode')
print(result)
result = count_code('cozexxcope')
print(result)