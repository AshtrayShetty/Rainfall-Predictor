from bs4 import BeautifulSoup
import requests
import csv
import os

try:
    os.chdir('.\\datasets')
except:
    print('directory not found')

try:
    web1=requests.get('https://karki23.github.io/Weather-Data/assignment.html').text
except:
    print("Page not found")
    exit()
    
soup1=BeautifulSoup(web1,'lxml')

list_link=soup1.ul.text.split('\n')

for link in list_link[1:len(list_link)-1]:
    
    if len(link.split(' '))>1:
        link=link.split(' ')
        link=link[0]+link[1]
    try:
        anchor=f'https://karki23.github.io/Weather-Data/{link}.html'
    except:
        print("Page not found")

    web2=requests.get(anchor).text
    soup2=BeautifulSoup(web2,'lxml')
    csv_file=open(f'{link}.csv','w')
    csv_writer=csv.writer(csv_file)

    for row in soup2.find_all('tr'):
        data=row.text.split('\n')
        csv_writer.writerow(i for i in data)

    csv_file.close()
    
