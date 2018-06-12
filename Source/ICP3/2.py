"""
2. Web scrapingWrite a simple program that parse a Wikipage mentioned below and follow the
instructions:https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India1.
 Import these librariesimport urllib.requestfrom bs4 import BeautifulSoupimport os2. Define a variable and put the link on that3.
  Get the urlex:  urllib.request.urlopen(‘step 2 variable’)4. Parse the source code using the Beautiful Soup library
  and save the parsed code in a variable5. Print out the title of the page6. Find all the links in the page (‘a’ tag)
7. Iterate over each tag(above) then return the link using attribute "href" using getFinding the right tableWe are looking for a
table to extract the information1. Extract information within all table2. To detect the right table we have to use the attribute
 class to point the table we want (In chrome, you can check the class name byright click on the required table of web page –>
 Inspect element –> Copy the class name OR go through the output of above command find the class name of right table.)
 here the attribute class name is class_='wikitable
sortable plainrowheaders'3. Iterate over table using for loop and "tr" attribute of the table4. Find All td and th print them out


"""


from bs4 import BeautifulSoup
import urllib.request
import os
import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source_code = urllib.request.urlopen(url)
plain_text = source_code
soup = BeautifulSoup(plain_text, "html.parser")
print(soup.find('title').string)
result_list = soup.findAll('a')

for i in result_list:
    link = i.get('href')
    print(link)

for tr in result_list:
    tdu = tr.findAll('td')
    thu = tr.findAll('th')
    print(tdu,thu)

table = pd.read_html("https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India", attrs= {'class' : 'wikitable sortable plainrowheaders'})

print(table)


