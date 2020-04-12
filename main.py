import random
import requests
from bs4 import BeautifulSoup
import re
list = []

page = requests.get("https://isthereanydeal.com/#/")
soup = BeautifulSoup(page.content, 'html.parser')

table = soup.find(class_="cntBoxContent")
sales = table.find_all(class_="bundle-container-outer bundle-preview giveaway")
bundles = table.find_all(class_="bundle-container-outer bundle-preview bundle")
links = table.find_all(class_="lg")

for i in range(0,len(links)):
    for link in links[i]:
        list.append(link)

print(list) #Prints text without links

print(links[0]) #Prints in order the items on page.
print(links[1])
print(links[2])
print(links[3])
print(links[4])
print(links[5])
print(links[6])
print(links[7])



count = 0
for i in links:
    list.append(i)
    count += 1
    if i == '<span class="lg">':
        list.pop(i[count])
list_pretty = []
length = len(list)
for i in range(length):
    if list[i].find('href') != -1:
        list_pretty.append(list[i])
    else:
        continue
print(list_pretty)