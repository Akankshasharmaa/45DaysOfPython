"""Output Lyrics"""
def recite(start_verse, end_verse):
    """
    input: start_verse, end_verse num as int
    return: list of lyrics
    """
    song = []
    first_line = "On the X day of Christmas my true love gave to me: "

    day_number = {1: "first", 2: "second", 3: "third", 4: "fourth",
    5: "fifth",6: "sixth", 7: "seventh", 8: "eighth", 9: "ninth",
     10: "tenth", 11: "eleventh", 12: "twelfth"}

    second_line = {
        1: "a Partridge in a Pear Tree.",
        2: "two Turtle Doves, ",
        3: "three French Hens, ",
        4: "four Calling Birds, ",
        5: "five Gold Rings, ",
        6: "six Geese-a-Laying, ",
        7: "seven Swans-a-Swimming, ",
        8: "eight Maids-a-Milking, ",
        9: "nine Ladies Dancing, ",
        10: "ten Lords-a-Leaping, ",
        11: "eleven Pipers Piping, ",
        12: "twelve Drummers Drumming, "
    }

    for verse_num in range(start_verse, end_verse + 1):
        first_sentence = first_line.replace("X", day_number[verse_num])

        for second_num in range(verse_num, 0, -1):
            if verse_num == 1:
                second_line[1] = "a Partridge in a Pear Tree."
            else:
                second_line[1] = "and a Partridge in a Pear Tree."
            first_sentence += second_line[second_num]
        song.append(first_sentence)
    return song
