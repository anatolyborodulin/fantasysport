from bs4 import BeautifulSoup
import requests

#url = 'http://www.khl.ru/stat/players/468/'
#url_content = requests.get(url)

# print(url_content.text)

#with open(url_content.text, encoding='utf-8') as raw_data:
with open('260917_stats.html', encoding='utf-8') as raw_data:
	soup = BeautifulSoup(raw_data, 'lxml')

script = soup.find('')



#for record in script:

print(script)


# with open('stats.txt','w',encoding='utf-8') as file:
# 	writer = 