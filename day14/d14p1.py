def xyz_there(str):
    for i in range (len(str)-2):
        if str[i] == 'x' and str[i+1] == 'y' and str[i+2] == 'z':
            if str[i-1] != '.':
                return True 
    return False

result = xyz_there('abcxyz')
print(result)
result = xyz_there('abc.xyz')
print(result)
result = xyz_there('xyz.abc')
print(result)
result = xyz_there('xyz.xyz')
print(result)
result = xyz_there('.xyzxyz')
print(result)