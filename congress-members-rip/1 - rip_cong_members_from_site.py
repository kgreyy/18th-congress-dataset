from bs4 import BeautifulSoup
import requests as r
import pandas as pd

resp = r.get('https://www.congress.gov.ph/members/')
bsob = BeautifulSoup(resp.content, features="html.parser")

tab = bsob.find_all('table', class_='table-responsive')
tds = tab[0].find_all('td')
tds.pop(0) # skip header

assert len(tds)%2==0

pairs = []
for o in range(0, len(tds)-1, 2):
    pairs.append((tds[o], tds[o+1]))

def get_data(pair):
    out = {}
    one, two = pair
    out['rep_name'] = one.a.text
    if two.text.find('District')==-1:
        out['partylist'] = two.text.lstrip('Party List -  ')
        out['rep_region'], out['rep_subdistrict'] = 2*['N/A']
    else:
        out['rep_region'], out['rep_subdistrict'] = two.text.split(', ')
        out['partylist'] = 'N/A'
    i = one.a['href'].find('=') # ../members/search.php?id=...
    out['link'] = one.a['href'][i+1:]
    return out

data = list(map(get_data, pairs))
df = pd.DataFrame(data)
df.to_csv('congress_members.csv', index=False)
