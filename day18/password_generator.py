import random
import string

def password_gernarator(pass_len, mylist):
    random.shuffle(mylist)
    password = []
    for i in range(pass_len):
        password.append(random.choice(mylist))
    return "".join(password)

if __name__ == '__main__':
    char_list = list(string.ascii_letters + string.digits +string.punctuation)
    alphabet_list = list(string.ascii_letters)
    # user input: pass type and pass len
    pass_type = input("Strong or weak? ")
    pass_len = int(input())
    if pass_type == 'weak':
        password = password_gernarator(pass_len, alphabet_list)
        print(password)
    elif pass_type == 'strong' and pass_len <= 7:
        print("For strong pass length >= 8")
    elif pass_type == 'strong' and pass_len >= 8:
        password = password_gernarator(pass_len, char_list)
        print(password)
    
