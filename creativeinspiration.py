#Creative Inspiration 2017
#A program created by Tyler Jackson


INPUT_FILENAME = 'mobydick.txt'
moby_dick_file = open(INPUT_FILENAME, 'r')
moby_dick_text = moby_dick_file.read()
moby_dick_file.close()

INPUT_FILENAME2 = 'scarlettletter.txt'
scarlett_letter_file = open(INPUT_FILENAME2, 'r')
scarlett_letter_text = scarlett_letter_file.read()
scarlett_letter_file.close()

INPUT_FILENAME3 = 'aliceinwonderland.txt'
alicein_wonderland_file = open(INPUT_FILENAME3, 'r')
alicein_wonderland_text = alicein_wonderland_file.read()
alicein_wonderland_file.close()

INPUT_FILENAME4 = 'ataleoftwocities.txt'
a_taleoftwocities_file = open(INPUT_FILENAME4, 'r')
a_taleoftwocities_text = a_taleoftwocities_file.read()
a_taleoftwocities_file.close()


text_files = [moby_dick_text, scarlett_letter_text, alicein_wonderland_text, a_taleoftwocities_text]

import json
CACHE_FNAME = "cachewords.json"
try:
    cache_file = open(CACHE_FNAME, 'r')
    cache_contents = cache_file.read()
    cache_file.close()
    CACHE_DICT = json.loads(cache_contents)
except:
    CACHE_DICT = {}



d = {}
for a_file in text_files:
    for word in a_file.split():
        if word in d:
            d[word] +=  1
        else:
            d[word] = 1


while True:
    selected_words = input("Enter a prompt: ")
    words_to_look_back = input("How many words would you like to look back(in digit form)?: ")
    num_to_look_back = int(words_to_look_back)
    indexed_words = selected_words.split()[-num_to_look_back:]
    joined_words = " ".join(indexed_words)
    print ("(searching for '{}') ".format(joined_words))

    split_words = joined_words.split()
    word_tuple = tuple(split_words)

    if joined_words in CACHE_DICT:
        sorted_cache = sorted(CACHE_DICT[joined_words], key = lambda x: CACHE_DICT[joined_words][x], reverse = True)
        for x in sorted_cache:
            print (joined_words + " " + x + " " + "*" + "{}".format(CACHE_DICT[joined_words][x]))
        if len(sorted_cache) == 0:
            print ('Sorry, no words were found. Try another prompt.')
    else:
        creative_words = []

        import re
        for a_file in text_files:
            creative_index = [x.start() for x in re.finditer(joined_words, a_file)]
            for x in creative_index:
                whole_phrase = x + len(joined_words)
                actual_phrase = a_file[whole_phrase + 1:]
                last_space = actual_phrase.find(" ")
                creative_words += [a_file[whole_phrase + 1: last_space + whole_phrase + 1]]



        word_freq = {}
        for x in creative_words:
            if x in d:
                word_freq[x] = d[x]


        final_dict = {}
        final_dict[word_tuple] = {}
        for x in creative_words:
            if x in d:
                final_dict[word_tuple][x] = d[x]



        sorted_words = sorted(word_freq.keys(), key = lambda x: word_freq[x], reverse = True)

        if len(sorted_words) == 0:
            print ("Sorry, no words were found. Try another prompt.")

        else:

            print(joined_words + "...")
            for x in sorted_words:
                print (joined_words + " " + x + " " + "*" + "{}".format(word_freq[x]))


            cache_file = open(CACHE_FNAME, 'w')
            CACHE_DICT[joined_words] = {}
            for x in creative_words:
                if x in d:
                    CACHE_DICT[joined_words][x] = d[x]
            cache_file.write(json.dumps(CACHE_DICT))
            cache_file.close()
