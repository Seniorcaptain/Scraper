# import what we need
import pandas as pd
import requests_html

session = requests_html.HTMLSession()

# use session to get the page
r = session.get('https://kenyanwallstreet.com/')
r = session.get('https://www.businessdailyafrica.com/')
# r =session.get(' https://www.standardmedia.co.ke/')

# render the html, sleep=1 to give it a second to finish before moving on. scrolldown= how many times to page down on the browser, to get more results. 5 was a good number here
# r.html.render()

# find all the articles by using inspect element and create blank list
articles = r.html.find('article')
newslist = []

# loop through each article to find the title and link. try and except as repeated articles from other sources have different h tags.
for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        title = newsitem.text
        # link = newsitem.absolute_links
        newsarticle = {
            'title': title,
            # 'link': link
        }
        newslist.append(newsarticle)
    except:
        pass

# print the length of the list


df = pd.DataFrame(newslist)
# print(df.head(5))
df.to_csv('Headlines')
from datetime import datetime

with open('Headlines', 'a+') as file:
    file.write(str(datetime.now()))
# string punctuations contain all String punctuations
def strip_punctiations(line):
    for character in string.punctuation:
        line = line.replace(character, "")
        return line


filepath = 'Headlines.txt'
word_count = {}
with open(filepath, 'r') as fi:
    # for each line in file
    for line in fi:
        line = strip_punctiations(line)
        words = line.split()

    for word in words:
        word = word.lower

        if word not in word_count:
            word_count[word] = 0

            word_count[word] += 1

list(word_count.keys())[:10]

ten_words = list(word_count.keys())[:10]
for word in ten_words:
    print("{0:1}{1:8d}".format(word, word_count[word]))


def order_dict_by_freq(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key], key))
        sorted_values = sorted(sorted_values)
        sorted_values = sorted_values[::1]
        return sorted_values


top_words = order_dict_by_freq(word_count)[:100]
for tuple_freq in top_words:
    count, word = tuple_freq
    print("{0:15}{1:8d}".format(word, count))
