def max_end3(arr):
    if len(arr) == 3:
        if arr[0] >= arr[2]:
            newarr = [arr[0], arr[0], arr[0]]
            return newarr
        elif arr[2] > arr[0]:
            newarr = [arr[2], arr[2], arr[2]]
            return newarr
        else:
            return arr
    else:
        return False

result = max_end3([1, 2, 3])
print(result)
result = max_end3([11, 5, 9])
print(result)
result = max_end3([2, 11, 2])
print(result)