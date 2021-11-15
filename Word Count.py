Text = """title
0,Safaricom debt rises five times to Sh76bn
1,Safaricom debt rises five times to Sh76bn
2,State blocks Kenya Power from hiring McKinsey as adviser
3,Economy Oil dealers get billions to keep fuel prices unchanged
4,"Corporate University of Nairobi, KU losses hit Sh4.3 billion"
5,News Blow to jobless Kenyan nurses as UK halts recruitment
6,Corporate INTERVIEW: Why KRA is eyeing the nice things you post on Facebook
7,Profiles On propelling a family’s legacy
8,Economy Homes pay Sh5bn more for electricity theft in State deal
9,Art Hybrid art auction earns Sh23 million
10,Economy China firm seeks Sh1.5bn for idle tools at JKIA
11,Corporate USIU picks top British firm to lead global hunt for vice chancellor
12,News Civil servant fights EACC over Sh500m in 22 bank accounts
13,Retail chain Mulleys shuts half of its outlets
14,KQ adds Ethiopia flights as workers flee Tigray fight
15,Assets agency to keep Sh3.1m found hidden in Nigerian suspect’s jacket
16,2 millers lock horns over maize flour brand name
17,City Hall staff working at NMS threaten strike
18,"Jambojet puts off plan to resume direct Entebbe, Kigali flights"
19,CMA caps firms shares buyback price at 10pc
20,"Cooking oil, bread, milk price rise signals expensive Christmas"
21,"Mitumba imports up 80pc on weak shilling, end of ban"
22,MPs summon Munya over coffee marketers’ licencing extension
23,Nyamira governor Nyaribo explains Sh6.5m Sept pay
24,Kenyans lose Sh1bn in ‘hot air’ payments to Prisons suppliers
25,State blocks Kenya Power from hiring McKinsey as adviser
26,New KCC boss gets third term despite suit
27,Owners of firms supplying Kenya Power to be revealed
28,"Portland Cement defaults on loan, cuts staff by 78pc"
29,USIU picks top British firm to lead global hunt for vice chancellor
30,Dimension Data eyes SMEs with cybersecurity service hub
31,MUSYOKA: Do customers choose a product or a brand?
32,NDUNG'U & GODOFA: Combatting counterfeits in the online marketplace
33,ODOTE: Society needs to appreciate teachers
34,EDITORIAL: Kenya Power system losses ought to drive turnaround
35,"KOECH: How Covid-19 has changed estate, succession planning"
36,EDITORIAL: KAA penalty unacceptable
37,Sale of 500 prison cows flops as one bidder shows up
38,Kenyans abroad invest most in stocks and private equity
39,Tea price drops for fifth week in a row on global glut
40,HF begins hunt for a strategic investor
41,"Uganda, UK coffee pact brews rivalry with Kenya"
42,Shilling falls to all time low on rise in dollar demand
43,MPUTHIA: Legal challenges in use of drones
44,OPIYO: How to prepare for retirement risks
45,Kananu's rocky road to Nairobi County helm
46,Heartstrings comes back with a bang
47,"‘It’s a She’, breaks all sorts of molds"
48,How firms can reap from climate change
49,Electric cars gradually drive into Kenyan roads
50,Africa missing out on climate innovations
51,"Aviation sector at 90pc of pre-Covid levels, says PS"
52,Kenya charts new roadmap to tap blue economy resources
53,Africa records highest growth in September cargo volumes
54,Nyeri digital start-up puts small hotels on global map
55,Hybrid art auction earns Sh23 million
56,On propelling a family’s legacy
57,‘My baboon shot that won global award’
58,Architects sketch bright future in tailoring
59,Why you shouldn’t skip leg day
60,DR OTIENO: Managing gout
61,OPIYO: How to prepare for retirement risks
62,MPUTHIA: Legal challenges in use of drones
63,EDITORIAL: Kenya Power system losses ought to drive turnaround
64,EDITORIAL: KAA penalty unacceptable
65,Should you rent or buy a home?
66,SAP’s vision for a digitally transformed Africa
67,County goes for innovative village concept
68,Top 5 questions you should ask your mortgage partner
69,Nairobi County road map to unlocking traffic in city centre
70,Water projects cut human-wildlife conflict in the Mara
71,How a Turkana village has stayed unscathed despite biting drought
72,How NYS battled to eradicate desert locust infestation
2021-11-15 16:29:54.035625se are Life, Liberty and the pursuit of Happiness.--That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed, --That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it, and to institute new Government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their Safety and Happiness."""

# Cleaning text and lower casing all words
for char in '-.,\n':
    Text = Text.replace(char, ' ')
Text = Text.lower()
# split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s)
word_list = Text.split()
# Initializing Dictionary

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