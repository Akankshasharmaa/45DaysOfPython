import random
import string

if __name__ == '__main__':
    char_list = list(string.ascii_letters + string.digits +string.punctuation)
    alphabet_list = list(string.ascii_letters)
    # user input: pass type and pass len
    pass_type = input("Strong or weak? ")
    pass_len = int(input())

    if pass_type == 'weak':
        random.shuffle(alphabet_list)
        password = []

        for i in range(pass_len):
            password.append(random.choice(alphabet_list))
        print("".join(password))

    elif pass_type == 'strong' and pass_len <= 7:
        print("For strong pass length >= 8")

    elif pass_type == 'strong' and pass_len >= 8:
        random.shuffle(char_list)
    
        password = []
        for i in range(pass_len):
            password.append(random.choice(char_list))
        print("".join(password))
