import requests
from bs4 import BeautifulSoup
import os

def download_pdf(link, filename):
    response = requests.get(link)
    with open(f"RawRIDs/{filename}", 'wb') as f:
        f.write(response.content)
    print(f"Downloaded {filename}")

def scrape_pdfs(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = soup.find_all('a')
    
    for link in links:
        href = link.get('href')
        if "Relatório Individual Docente – RID" in link.text:
            filename = href.split('/')[-1]
            download_pdf(href, filename)

url = "https://www.unifal-mg.edu.br/ict/corpo-docente-ict/"
scrape_pdfs(url)