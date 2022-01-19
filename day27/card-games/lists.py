"""Card game"""
def get_rounds(number):
    """
     :param number: int - current round number.
     :return: list - current round and the two that follow.
    """
    num_list = [number, (number+1), (number+2)]
    return num_list

def concatenate_rounds(rounds_1, rounds_2):
    """
    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    new_list = rounds_1 + rounds_2
    return new_list

def list_contains_round(rounds, number):
    """
    :param rounds: list - rounds played.
    :param number: int - round number.
    :return:  bool - was the round played?
    """
    if len(rounds) > 0:
        for item in rounds:
            if item == number:
                return True
        return False
    return False

def card_average(hand):
    """
    :param hand: list - cards in hand.
    :return:  float - average value of the cards in the hand.
    """
    count = len(hand)
    return sum(hand)/count

def approx_average_is_average(hand):
    """
    :param hand: list - cards in hand.
    :return: bool - if approximate average equals to the `true average`.
    """
    list_len = len(hand)
    median = hand[(list_len-1)//2]
    first_last_avg = (hand[0] + hand[-1]) / 2
    new_list = [first_last_avg , median]
    myaverage = card_average(hand)
    if myaverage in new_list:
        return True
    return False

def average_even_is_average_odd(hand):
    """

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """
    even = hand[::2]
    odd = hand[1::2]
    even_avg = card_average(even)
    odd_avg = card_average(odd)
    if even_avg == odd_avg:
        return True
    return False

def maybe_double_last(hand):
    """

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] = 22
    return hand
