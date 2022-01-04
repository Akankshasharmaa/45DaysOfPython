def end_other(a, b):
    str_a = a.lower()
    str_b = b.lower()

    if str_a.endswith(str_b) or str_b.endswith(str_a):
        return True
    
    return False

    
result = end_other('abcab', 'ab')
print(result)
result = end_other('AbC', 'HiaBc')
print(result)
result = end_other('abc', 'abXabc')
print(result)