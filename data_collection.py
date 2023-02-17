import vlr_scraper as vs

# get all of the regions
'''indexing the regions
1=europe
2=north america
3=brazil
4=asia pacific
5=korea
6=china
7=japan
8=latin america-south
9=latin america-north
10=oceania
11=mena
12=gc'''

# can also iterate through the regions, but sometimes the website doesn't fully load which breaks the bot...
region_number = 1
save_file_as = 'player_data_eu.csv'

df = vs.get_data(region_number)
df.to_csv(save_file_as, index=False)
# df.to_csv('output.csv')
print(df)
