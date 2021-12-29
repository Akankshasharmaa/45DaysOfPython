def middle_way(arr1, arr2):
    if len(arr1) == 3 and len(arr2) == 3:
        newarr = [arr1[1], arr2[1]]
        return newarr
    else:
        return False

result = middle_way([1, 2, 3], [4, 5, 6])
print(result)
result = middle_way([7, 7, 7], [3, 8, 0])
print(result)
result = middle_way([5, 2, 9], [1, 4, 5])
print(result)