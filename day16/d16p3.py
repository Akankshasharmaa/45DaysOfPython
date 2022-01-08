string = "Practice Problems to Drill List Comprehension in Your Head."

count = 0

for i in range(len(string)):
    if string[i] == ' ':
        count += 1
print(count)

my_space = len([space for space in string if ' ' in space])

print(my_space)