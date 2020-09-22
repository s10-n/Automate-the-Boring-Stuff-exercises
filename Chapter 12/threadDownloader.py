#! python3
# threadDownloader.py - downloads all the responses to an imageboard thread given a board and the thread ID
import requests, bs4, webbrowser
board = input('Please enter a board name (no slashes necessary): ')
thread_number = input('Please enter a thread number: ')
thread = requests.get('https://boards.4channel.org/' + board + '/thread/' + thread_number)
thread.raise_for_status()
thread_soup = bs4.BeautifulSoup(thread.text, 'html.parser')
raw_posts = thread_soup.select('blockquote')
posts = {}
for index,post in enumerate(raw_posts):
    posts[post.attrs['id'][1:]] = post.getText()
print(str(len(posts)) + ' posts saved.')
