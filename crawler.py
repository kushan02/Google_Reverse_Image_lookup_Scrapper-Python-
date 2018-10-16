from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import urllib
import time
import re

def extractLinkTitle(value):
    return str(re.sub("<.*?>", "", str(value)))


#url = 'http://www.google.com/search?tbs=sbi:AMhZZisfGTm-qffp1pxH_1h9-VJrDmqtw_1uAzNuQpEcQU2m_18AFMaeeF6BMV1b1kEqyXpdixCfA4-zCnVU8cT-q9Ub66mjS7regNNDjjbyqJDtqiJfqECIxJOG6czzyfbTEk_1rBorgwdCj0cusWkJZr5ycxVy3YZZGTHF6uK_1JWHaM2RvtwiiW10frlb5GLiZrW-T7WA4ZLgOK8VkKlzLlZCdF6AwKqgUqvkXsePgRyhmS4nrD6cAEVbWLTQKSV5FsIkAboXktXs0AMWKdpR6c7k2UBWIn4aXSgJyIpVvmObGWF4Aw3QwLzGbrAjvwnzi5icqCWl2Pnjl'

filePath = 'bookimage.jpg'
#filePath = 'javabook.jpg'
searchUrl = 'http://www.google.com/searchbyimage/upload'
multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
response = requests.post(searchUrl, files=multipart, allow_redirects=False)
fetchUrl = response.headers['Location']
#webbrowser.open(fetchUrl)

print(fetchUrl)

url = fetchUrl


path_to_chromedriver = 'C:\\Users\\Kushan Mehta\\Desktop\\chromedriver_win32\\chromedriver.exe'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)
browser.get(url)

html = browser.page_source
soup = BeautifulSoup(html, "html5lib")

#links = soup.findAll("a")
#for link in links :
#    print(link)

value = soup.find('a', {'class': 'fKDtNb'})
print(value.get('href'))

print("*********************")
print("")
x = str(value)
contentTitle = str(re.sub("<.*?>", "", x))
#print(value.get('text'))
print("TITLE: ",contentTitle)
print("")
print("*************************")

print("\nLINKS:\n")

links = soup.select('.r a')
tab_counts = min(10, len(links))
for i in range(tab_counts):
    #h3 = links[i].find("h3", class_= "LC201b")
    #print(extractLinkTitle(h3))
    print(links[i].get('href'))
# print(extractLinkTitle(links[i]))


print("\n##########################\n")

print("\nTITLE: ",contentTitle,"\n")
print("\nLINK TITLES:\n")
links = soup.findAll('h3',{'class' : 'LC20lb'})
for link in links :
    print(extractLinkTitle(link))

browser.quit()

#print(soup.prettify())
