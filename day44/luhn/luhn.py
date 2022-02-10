"""Luhn"""
import string
class Luhn:
    """Checking a given card number is valid or not"""
    def __init__(self, card_num):
        """card num"""
        self.card_num = card_num

    def valid(self):
        """Validation of a card number"""
        for i in range(len(self.card_num)):
            if self.card_num[i] in string.punctuation + string.ascii_lowercase + string.ascii_uppercase:
                return False

        myobject = self.card_num.split(" ")

        num_list = []
        for num in myobject:
            for i in range(len(num)):
                num_list.append(int(num[i]))

        if len(num_list) <= 1:
            return False

        for i in range(len(num_list)-2, -1, -2):
            num_list[i] = num_list[i] * 2
            if num_list[i] > 9:
                num_list[i] = num_list[i] - 9

        mysum = sum(num_list)
        print(mysum)
        if mysum%10 == 0:
            return True
        return False
