string = "Practice Problems to Drill List Comprehension in Your Head."

string_list = string.split()
newlist = [item for item in string_list if len(item) < 5]
# for item in string_list:
#     if len(item) < 5:
#         newlist.append(item)
print(newlist)