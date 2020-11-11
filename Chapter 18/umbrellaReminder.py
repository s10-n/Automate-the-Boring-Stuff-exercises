#! python3
# umbrellaReminder.py - checks whether it’s raining that day and texts you a reminder to pack an umbrella before leaving the house if it is

import requests, bs4, re, textMyself

weather_page = requests.get('https://weather.gc.ca/city/pages/bc-74_metric_e.html')
weather_page.raise_for_status()
weather_page_soup = bs4.BeautifulSoup(weather_page.text, 'html.parser')
current_conditions = str(weather_page_soup.select('img ~ p.visible-xs.text-center')[0])
if not re.search('[R|r]ain',current_conditions):
    textmyself('Heads up - looks like it might rain this morning. Bring an umbrella!')
