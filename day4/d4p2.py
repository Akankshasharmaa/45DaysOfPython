def array_count9(arr):
    count = 0
    for num in arr:
        if num == 9:
            count = count + 1
    return count
        

count = array_count9([1, 2, 9])
print(count)
count = array_count9([1, 9, 9])
print(count)
count = array_count9([1, 9, 9, 3, 9])
print(count)