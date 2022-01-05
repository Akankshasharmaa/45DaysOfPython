def xyz_there(str):
    for i in range (len(str)-2):
        if str[i] == '.' and str[i+1] == 'x' and str[i+2] == 'y' and str[i+3] == 'z':
            return False
        elif str[i] == 'x' and str[i+1] == 'y' and str[i+2] == 'z':
            print(str[i])
            return True 


result = xyz_there('abcxyz')
print(result)
result = xyz_there('abc.xyz')
print(result)
result = xyz_there('xyz.abc')
print(result)