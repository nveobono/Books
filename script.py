"""
Script to download all programming documents from https://goalkicker.com/
"""
import urllib
import requests
from bs4 import BeautifulSoup

url = "https://goalkicker.com/"
mainpage = requests.get(url)
soup = BeautifulSoup(mainpage.content, 'html.parser')

docPages = []
for div in soup.findAll("div","bookContainer"):
    for a in div.find_all("a", href=True):
        docPages.append(url+a['href'])    

docsUrls = []
for docPageUrl in docPages:
    docPage = requests.get(docPageUrl)
    soup2 = BeautifulSoup(docPage.content, 'html.parser')
    docName = soup2.find(class_='download')["onclick"].split("=")[1][1:-1]
    print("Retrieved document name: " + docName)
    docsUrls.append((docName,docPageUrl))

for docName,docUrl in docsUrls:
    print("Downloading file... " + docName)
    urllib.request.urlretrieve (docUrl+docName, docName)
    print("Saved to " + docName)
