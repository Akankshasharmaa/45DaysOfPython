nums = [i for i in range(1,1001)]

mylist = list(map(str, nums))

result = [item for item in mylist if '6' in item]

num_list = list(map(int, result))

print(num_list)