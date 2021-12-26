def array_front9(arr):
    count = 0
    for num in arr:
        count = count + 1
        if count <= 4:
            if num == 9:
                return True
        else:
            return False
    return False   

count9 = array_front9([1, 2, 9, 3, 4])
print(count9)
count9 = array_front9([1, 2, 3, 4, 9])
print(count9)
count9 = array_front9([])
print(count9)