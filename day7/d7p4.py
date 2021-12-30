def make_tags(str1, str2):
    
    newstr = '<' + str1 + '>' + str2 + '</'+ str1 + '>'
    return newstr

result = make_tags('i', 'Yay')
print(result)
result = make_tags('i', 'Hello')
print(result)
result = make_tags('', '')
print(result)