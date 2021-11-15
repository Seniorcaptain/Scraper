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
