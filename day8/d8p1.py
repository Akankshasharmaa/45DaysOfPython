def first_half(str):
    if len(str) % 2 == 0:
        newstr = str[:len(str)/2]
        return newstr
    else:
        return False


result = first_half('WooHoo')
print(result)
result = first_half('HelloThere') # 'Hello'
print(result)
result = first_half('abcdef') # 'abc'
print(result)