def array123(arr):
    myarr = [1,2,3]
    for i in range(len(arr)):
        if arr[i: (i+3)] == myarr:
            return True
    return False

result = array123([1, 1, 2, 3, 1])
print(result)
result = array123([1, 1, 2, 4, 1])
print(result)
result = array123([1, 1, 2, 1, 2, 3])
print(result)