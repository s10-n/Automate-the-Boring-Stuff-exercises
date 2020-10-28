#! python3
# threadedDownloadXkcd.py - downloads xkcd comics using multiple threads
import requests, os, bs4, threading
os.makedirs('xkcd', exist_ok = True) # store comics in ./xkcd
def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # download the page
        print('Downloading page https://xkcd.com/%s...' % (urlNumber))
        res = requests.get('https://xkcd.com/%s' % (urlNumber))
        res.raise_for_status()
        soup = bs4.BeautifulSoup(res.text, 'html.parser')
        # find the URL of the comic image
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print('Could not find comic image.')
        else:
            comicUrl = comicElem[0].get('src')
            # download the image
            print('Downloading image %s...' % (comicUrl))
            res = requests.get('https:' + comicUrl)
            res.raise_for_status()
            # save the image to ./xkcd
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)),'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
# create and start the thread objects
downloadThreads = [] # a list of all the thread objects
for i in range(0,140,10): # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1 # there is no comic 0, so set it to 1
    downloadThread = threading.Thread(target=downloadXkcd, args = (start, end))
    downloadThreads.append(downloadThread)
    downloadThread.start()
# wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
