def non_start(str1, str2):
    if len(str1) >= 1 and len(str2) >= 1:
        newstr = str1[1:len(str1)] + str2[1:len(str2)]
        return newstr
    else:
        return False

result = non_start('Hello', 'There')
print(result)
result = non_start('java', 'code')
print(result)
result = non_start('shotl', '')
print(result)