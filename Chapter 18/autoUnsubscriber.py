#! python3
# autoUnsubscriber.py - scans through your email account, finds all the unsubscribe links in all your emails, and automatically opens them in a browser

import imapclient,bs4,pyzmail,re,webbrowser,sys

# get all of your emails
imap_object = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imap_object.login('test@gmail.com', sys.argv[1])
imap_object.select_folder('INBOX', readonly=True)
message_UIDs = imap_object.search(['ALL'])
raw_messages = imap_object.fetch(message_UIDs, ['BODY[]'])

# for each email, scan for unsubscribe links
for UID in message_UIDs:
    message = pyzmail.PyzMessage.factory(raw_messages[UID][b'BODY[]'])
    if message.html_part:
        message_soup = bs4.BeautifulSoup(message.html_part.get_payload().decode(message.html_part.charset), 'html.parser')
        unsubscribe_links = list(filter(lambda a: re.search('[U|u]nsubscribe|[R|r]emove',str(a)),message_soup.find_all('a')))

        # open the unsubscribe links in your browser
        for i in unsubscribe_links:
            webbrowser.open(unsubscribe_links[0].get('href'))
        
# logout of your email
imap_object.logout()
