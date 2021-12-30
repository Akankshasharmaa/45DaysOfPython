def sum3(arr):
    if len(arr) == 3:
        sumOfArr = arr[0] + arr[1] + arr[2]
        return sumOfArr
    else:
        return False

result = sum3([1, 2, 3])
print(result)
result = sum3([5, 11, 2]) # 18
print(result)
result = sum3([7, 0, 0]) # 7
print(result)