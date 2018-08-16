import urllib.request
from bs4 import BeautifulSoup

url = "https://old.reddit.com/top/"
#download the URL and extract the content to the variable html 
request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()
#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(html,'html.parser')
#get the HTML of the table called site Table where all the links are displayed
main_table = soup.find("div",attrs={'id':'siteTable'})
#Now we go into main_table and get every a element in it which has a class "title" 
links = main_table.find_all("a",class_="title")
#from each link extract the text of link and the link itself
#List to store a dict of the data we extracted 
extracted_records = []
for link in links: 
    title = link.textT
    url = link['href']
    record = {
        'title':title,
        'url':url
        }
    extracted_records.append(record)
print(extracted_records)



