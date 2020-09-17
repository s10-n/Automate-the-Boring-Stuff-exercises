#! python3
# downloadXkcd.py - downloads every single XKCD comic
import requests, os, bs4
url = 'https://xkcd.com' # starting URL
os.makedirs('xkcd',exist_ok=True) # store comics in an 'xkcd' folder
while not url.endswith('#'):
    # download the page
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    # find the URL of the comic image
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
    # download the image
    print('Downloading image %s...' % (comicUrl))
    # save the image to /xkcd
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # get the 'Prev' button URL
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')
print('Done.')
