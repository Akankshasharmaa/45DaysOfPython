"""Count words"""
import string
import re

def count_words(sentence):
    """
    input: string
    return: dict of word frequencies
    """
    myword = {}
    sentence = sentence.lower()
    new_sentence = ""
    for i, char in enumerate(sentence):
        if i < len(sentence) - 2:
            next_char = sentence[i + 1]
            if char == "'" and next_char in ("s","t"):
                new_sentence += char
                continue
        if char not in string.punctuation:
            new_sentence += char
        elif char in (",", "_"):
            new_sentence += " "
    words = re.split(r"\s|\t|\n", new_sentence)
    for word in words:
        word = word.strip("'")
        if len(word) == 0:
            continue
        if word not in myword:
            myword[word] = 1
        elif word in myword:
            myword[word] += 1
    return myword
