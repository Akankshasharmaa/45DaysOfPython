birthdays = {
    'Manish': '25/12/90', 
    'Arpit':'10/02/94', 
    'Vaishali':'27/03/92'
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for item in birthdays:
    print(item)

name = input("Who's birthday do you want to look up?\n")
for item in birthdays:
    if item == name:
        print(item + "'s birthday is " + birthdays[item] +".")
