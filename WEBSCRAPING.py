from bs4 import BeautifulSoup
import requests
#features="html.parser"


#with open('practice.html') as html_file:
#   soup = BeautifulSoup(html_file,'lxml')
#match=soup.title
#match1=soup.title.text
#print(match)
#print(match1)

source=requests.get('https://www.google.com').text
soup = BeautifulSoup(source,'lxml')
#print(soup.prettify())

match=soup.title.text
print(match)

match1=soup.div
print(match1)

match2=soup.find('div',class_='footer')
print(match2 )

