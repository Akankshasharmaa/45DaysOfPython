def reverse3(arr):
    newarr = []
    if len(arr) == 3:
        for i in range(len(arr) - 1, -1, -1):
            newarr.append(arr[i])
        return newarr
    else:
        return False

result = reverse3([1, 2, 3])
print(result)
result = reverse3([5, 11, 9])
print(result)
result = reverse3([7, 0, 0])
print(result)