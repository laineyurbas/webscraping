import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request


chapters = list(range(1,21)) # so chapters is a list of numbers bw 1 and 21

random_chapter = random.choice(chapters)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

url = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(url, headers=headers)

webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
print(soup.title.text)

page_verses = soup.findAll('div',class_='main')
#print(page_verses)

for verses in page_verses:
    verse_list = verses.text.split(".")

mychoice = random.choice(verse_list[:-5]) #start at lower verse, of all elements dont go to end 

verse = f'Chapter: {random_chapter} Verse: {mychoice}'

print(verse)

import keys
from twilio.rest import Client


client = Client(keys.accountSID, keys.authtoken)

TwilioNumber = "+14072891580"

mycellphone = '+13038804356'

textmessage = client.messages.create(to=mycellphone, from_=TwilioNumber,
                                     body = verse)
print(textmessage.status)

call = client.calls.create(to=mycellphone, from_=TwilioNumber)
                                   
