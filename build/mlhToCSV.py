from bs4 import BeautifulSoup as bs
import requests as r
import csv

WRITEFILE = "../MLHNA2019.csv"

#=========================================================================

def process_event(event):
    return [
        event['title'],     # event title
        event['href'],      # event link
        event.find('meta', {'itemprop':'startDate'})['content'],    # start date
        event.find('meta', {'itemprop':'endDate'})['content'],      # end date
        event.find('span', {'itemprop':'city'}).text,               # city
        event.find('span', {'itemprop':'state'}).text               # state
    ]

#=========================================================================

# get MLH NA 2019 schedule
page = bs(r.get('https://mlh.io/seasons/na-2019/events').content)

events = page.find_all('a', {'class':'event-link'})

with open(WRITEFILE, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for event in events:
        writer.writerow(process_event(event))


