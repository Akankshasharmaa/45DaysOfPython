def rotate_left3(arr):
    if len(arr) == 3:
        newarr = [arr[1], arr[2], arr[0]]
        return newarr
    else:
        return False

result = rotate_left3([1, 2, 3])
print(result)
result = rotate_left3([5, 11, 9])
print(result)
result = rotate_left3([7, 0, 0])
print(result)