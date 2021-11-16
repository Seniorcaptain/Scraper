import string

filepath = 'Headlines.csv'
word_count = {}


def strip_punctiations(line):
    for character in string.punctuation:
        line = line.replace(character, "")
        return line


with open(filepath, 'r') as fi:
    # for each line in file
    for line in fi:
        line = strip_punctiations(line)
        words = line.split()

    # Cleaning text and lower casing all words
for char in '-.,\n':
    filepath = filepath.replace(char, ' ')
filepath = filepath.lower()  # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
word_list = filepath.split()

from collections import Counter
Counter(word_list).most_common()

# Initializing Dictionary
d = {}

# counting number of times each word comes up in list of words (in dictionary)
for word in word_list:
    d[word] = d.get(word, 0) + 1

    word_freq = []
    for key, value in d.items():
        word_freq.append((value, key))

        word_freq.sort(reverse=True)
        print(word_freq)