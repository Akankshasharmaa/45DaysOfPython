"""Acronym"""
import string
import re
def abbreviate(words):
    """
    input: string
    return: abbrevation f the string
    """
    acronym = ""
    words = re.split(r" |-", words)
    for word in words:
        word = word.strip("_")
        if word != "" and word[0] not in string.punctuation:
            acronym += (word[0]).upper()
    return acronym
