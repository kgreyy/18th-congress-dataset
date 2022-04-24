import pandas as pd

def convt_name(entry):
    i = entry.find('City Of ')
    if i!=-1:
        entry = entry[i+len('City Of '):] + ' City'
    i = entry.find('Del')
    if i!=-1:
        entry = entry[0:i]+entry[i:i+3].lower()+entry[i+3:]
    i = entry.find('De')
    if i!=-1:
        entry = entry[0:i]+entry[i:i+2].lower()+entry[i+2:]
    if entry == 'Cotabato (North Cot.)':
        return "North Cotabato"
    elif entry == 'Davao (Davao del Norte)':
        return 'Davao del Norte'
    elif entry == 'Compostela Valley':
        return 'Davao de Oro'
    elif entry == 'Manila City':
        return 'Manila'
    elif entry == 'Samar (Western Samar)':
        return 'Samar'
    elif entry == 'San Jose del Monte  City':
        return 'San Jose Del Monte City'
    elif entry == 'Lapu-Lapu City (Opon)':
        return 'Lapu-Lapu City'
    elif entry == 'Taguig City':
        return 'Taguig'
    return entry
def fix_case(entry):
    if type(entry) is float:
        return entry
    if entry[0] in [str(x) for x in range(10)]:
        entry = entry[0] + entry[1].lower() + entry[2:]
    return entry

df = pd.read_csv('comelec_elected.csv')
df['district'] = df[df['name'].str.contains('DISTRICT')]['name'].str.title()
df['district'] = df['district'].fillna(method='ffill')
df['district'] = df['district'].map(fix_case)

df = df.drop(df[df['name'].str.contains('DISTRICT')].index)
df = df.drop(df[df['name'] == 'NATIONAL CAPITAL REGION - MANILA'].index)

df['region'] = df[df['name'].str.contains('REGION')]['name']
df.loc[df['name'] == 'BARMM', 'region'] = 'BARMM'
df['region'] = df['region'].fillna(method='ffill')

df = df.drop(df[df['name'].str.contains('REGION')].index)
df = df.drop(df[df['name'] == 'BARMM'].index)

subdistricts = df[~df['name'].str.contains(',')]['name']
df['subdistrict'] = df[~df['name'].str.contains(',')]['name'].str.title()
df['subdistrict'] = df['subdistrict'].fillna(method='ffill')
df['subdistrict'] = df['subdistrict'].map(convt_name)
df.loc[df['subdistrict'] == 'Taguig City-Pateros', 'subdistrict'] = 'Taguig-Pateros'

df = df.drop(df[~df['name'].str.contains(',')]['name'].index)
df.to_csv('comelec_elected_clean.csv', index=False)
