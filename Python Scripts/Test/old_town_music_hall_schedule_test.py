import requests
from bs4 import BeautifulSoup
import re
# import json

url = "http://www.oldtownmusichall.org/schedule.html"
content = requests.get(url).text

soup = BeautifulSoup(content, 'html.parser')

# newDictionary=json.loads(str(soup))

main_table = soup.find("div",attrs={'id':'concert-listings'})

concerts = main_table.find_all("div",class_="concert-block repeatable")

#details = concerts.find_all("div",class_="filmcenter",text=True,recursive=False)


info = []
for body in concerts:
	try: 
		con= 'CONCERT'
		var = body.h4.get_text()  # print(body.h4.get_text())
	
		if re.search(r'\bCONCERT\b',var) is None:
			info.append(body)
	except AttributeError:
		pass


restructured_movie_list =[]
for title in info:
	var = title.find_all("strong")
	restructured_movie_list.append(var)
	# dictiorary ={
	# 	'title': title.select("p.span.strong")
	# }
	# info.append(dictiorary)
	# print("this is what i am itereating over; %s" % (title))

print(restructured_movie_list)

# #for info in details: 
#     title = info.textS
#     record = {
#         'title':title,
#         }
#	body.append(record)
# for i in info:

# info.find_all('p')
#body = title

# print(info)