def recite(start_verse, end_verse):

        

          


        

          

    base_template = "On the X day of Christmas my true love gave to me: "

        

          

    ordinal_numbers = {

        

          

        1: "first",

        

          

        2: "second",

        

          

        3: "third",

        

          

        4: "fourth",

        

          

        5: "fifth",

        

          

        6: "sixth",

        

          

        7: "seventh",

        

          

        8: "eighth",

        

          

        9: "ninth",

        

          

        10: "tenth",

        

          

        11: "eleventh",

        

          

        12: "twelfth",

        

          

    }

        

          

    next_template = {

        

          

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

        

          

        12: "twelve Drummers Drumming, ",

        

          

    }

        

          

    extra_and = "and "

        

          


        

          

    new_list = []

        

          

    for verse_num in range(start_verse, end_verse + 1):

        

          

        base_sentence = base_template.replace("X", ordinal_numbers[verse_num])

        

          

        # next_sentence = next_template[verse_num]

        

          

        # print(base_sentence)

        

          

        # print(next_sentence)

        

          

        # new_list.append(base_sentence)

        

          

        for next_sentence_num in range(verse_num, 0, -1):

        

          

            if verse_num > 1:

        

          

                next_template[1] = "and a Partridge in a Pear Tree."

        

          

            else:

        

          

                next_template[1] = "a Partridge in a Pear Tree."

        

          

            base_sentence += next_template[next_sentence_num]

        

          

        new_list.append(base_sentence)

        

          


        

          

    return new_list
