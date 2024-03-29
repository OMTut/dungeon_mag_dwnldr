#***************************************************
# This script downloads all the Dungeon Magazine PDFs
# from the Internet Archive. It will download the
# files to the folder 'pdfs' in the current directory.
#***************************************************
import requests
import os
import time

# URL format for Dungeon Magazine PDFs
# archive.org has 2 formats for DM pdfs
url1 = 'https://archive.org/download/dungeon-magazine-'
url2a = '/Dungeon_Magazine_'
url2b = '/Dungeon%20Magazine%20'
url3 = '.pdf'

deadlinks = 0
download_folder = './pdfs'

for i in range (1, 222):
   i = str(i).zfill(3)

   # Try the first URL format, if it fails, try the second format
   try:
      url=url1 + i + url2a + i + url3
      response = requests.get(url)
      response.raise_for_status()
   except requests.exceptions.HTTPError:
      url = url1 + i + url2b + i + url3
      response = requests.get(url)

   # If the response is 200, download the file
   if response.status_code == 200:
      print(f'\033[92mDownloading file\033[0m: {url}')
      with open(os.path.join(download_folder, f'Dungeon_Magazine_{i}.pdf'), 'wb') as f:
         f.write(response.content)
      time.sleep(30) # Sleep for 15 seconds to avoid getting blocked
   else:
      deadlinks += 1
      print(f'\033[91mError downloading file\033[0m: {url}')

print('Dead links:', deadlinks)