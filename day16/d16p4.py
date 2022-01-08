string = "Practice Problems to Drill List Comprehension in Your Head."
mylist = list(map(str, string))
vowel = ['a', 'e', 'i', 'o', 'u']
newlist = [item for item in mylist if item not in vowel]
# for i in range(len(mylist)-1):
#     if mylist[i] not in vowel:
#         newlist.append(mylist[i])

mystring = ''.join(newlist)
# for i in range(len(newlist)):
#     mystring += newlist[i]

# We can also do:
# mystring = ''.join([item for item in mylist if item not in vowel])
print(mystring)