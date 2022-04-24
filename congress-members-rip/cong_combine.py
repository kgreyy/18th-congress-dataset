import pandas as pd

df1 = pd.read_csv('congress_members.csv')
df2 = pd.read_csv('comelec_elected_clean.csv')
# matter of expression - Taguig, Taguig-Pateros = separate counting
df1.loc[df1['rep_region']=='Taguig-Pateros', 'rep_subdistrict'] = 'Lone District'
df1.loc[df1['rep_region']=='Taguig', 'rep_subdistrict'] = 'Lone District'
new_df = pd.merge(df1, df2,  how='left', left_on=['rep_subdistrict','rep_region'], right_on = ['district', 'subdistrict'])
# from wikipedia
new_df.loc[new_df['rep_name']=='Mercado, Roger G.', 'party'] = 'LAKAS'
new_df.loc[new_df['rep_name']=='Mercado, Roger G.', 'subregion'] = 'Southern Leyte'
new_df.loc[new_df['rep_name']=='Mercado, Roger G.', 'subdistrict'] = 'Lone District'
new_df.loc[new_df['rep_name']=='Cua, Junie E.', 'party'] = 'PDP–Laban'
new_df.loc[new_df['rep_name']=='Cua, Junie E.', 'subregion'] = 'Quirino'
new_df.loc[new_df['rep_name']=='Cua, Junie E.', 'subdistrict'] = 'Lone District'
toresolve = new_df[new_df['subdistrict'].isna() & new_df['partylist'].isna()]
assert len(toresolve)==0
new_df.to_csv('18th_congress_hor.csv', index=False)
