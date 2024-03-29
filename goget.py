import requests
from bs4 import BeautifulSoup

url='https://archive.org/details/DragonMagazine260_201801/Dragon%20Magazine%20429/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# count the divs where class is 'format-file'
divs = soup.find_all('a', class_='stealth download-pill')
#pdfs = soup.find_all('a', href=True)
#pdfs = [pdf['href'] for pdf in pdfs if pdf['href'].endswith('.pdf')]

num_divs = len(divs)
#num_pdfs = len(pdfs)
print(f"Number of divs: {num_divs}")
#print(f"Number of PDFs: {num_pdfs}")