def count_code(str):
    count = 0
    if len(str) >= 4:
        for i in range(len(str) - 3):
            if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
                count += 1
        return count
    else:
        return 0

result = count_code('codegrcofecoge')
print(result)
result = count_code('codexxcode')
print(result)
result = count_code('cozexxcope')
print(result)