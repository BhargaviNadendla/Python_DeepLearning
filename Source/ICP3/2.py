from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
from tabulate import tabulate

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
res = urllib.request.urlopen(url)  #open the url and get the source code
plain_text = res
soup = BeautifulSoup(plain_text, "html.parser") # pass the plain_text and html parser through beautiful soup
print(soup.find('title').string)   #print title of the html file
result_list = soup.findAll('a')    # Store all the anchor tags into result_list

for i in result_list:
    link = i.get('href')   #for each anchor tag get href
    print(link)    # printing href

result_table = soup.findAll('table', {'class': 'wikitable sortable plainrowheaders'}) #getting the desired table
for tr in result_table:
    table_data = tr.findAll('td')
    table_head = tr.findAll('th')
    print(table_data, table_head) # printing td and th for each row of the table



table = soup.find_all('table')[1]  #finding the desired table
df = pd.read_html(str(table),header=0)  #reading the content of the table with pandas
print(tabulate(df[0], headers='keys', tablefmt='psql')) #tabulating the table content and table header