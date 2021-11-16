import string

Text = """'StanChart Q3 net profit jumps to Sh6.4bn
1,StanChart Q3 net profit jumps to Sh6.4bn
2,NMS steps up collection of house data
3,"Companies World Bank, AfDB blacklist nearly 20 Kenya firms over fraud"
4,Companies Safaricom debt rises five times to Sh76bn
5,Companies State blocks Kenya Power from hiring McKinsey as adviser
6,Economy Oil dealers get billions to keep fuel prices unchanged
7,"Corporate University of Nairobi, KU losses hit Sh4.3 billion"
8,News Blow to jobless Kenyan nurses as UK halts recruitment
9,Corporate INTERVIEW: Why KRA is eyeing the nice things you post on Facebook
10,Profiles On propelling a family’s legacy
11,Economy Homes pay Sh5bn more for electricity theft in State deal
12,Art Hybrid art auction earns Sh23 million
13,DCI offers Sh60m in hunt for 3 terror suspects who escaped Kamiti
14,Retail chain Mulleys shuts half of its outlets
15,KQ adds Ethiopia flights as workers flee Tigray fight'"""
word_count = {}


def strip_punctiations(line):
    for character in string.punctuation:
        line = line.replace(character, "")
        return line


#with open(Text, 'r') as fi:
    # for each line in file
    #for line in fi:
      #  words = line.split()

    # Cleaning text and lower casing all words
for char in '-.,\n':
    Text = Text.replace(char, ' ')
Text = Text.lower()  # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
word_list = Text.split()

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