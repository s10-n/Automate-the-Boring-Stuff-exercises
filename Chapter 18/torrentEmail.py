#! python3
# torrentEmail.py - checks an email account for any torrent links you email it and downloads them automatically

import subprocess,imapclient,pyzmail,textMyself,sys

# log into email
imap_object = imapclient.IMAPClient('imap.gmail.com',ssl=True)
imap_object.login('test@gmail.com','sys.argv[1]')
imap_object.select_folder('INBOX',readonly=False)

# look for emails from me with a password in them
UIDs_from_me = list(imap_object.search(['FROM', 'me@email.com','BODY', 'password']))
messages_from_me = imap_object.fetch(UIDs_from_me, ['BODY[]'])

# find all of the torrent links in each email
for UID in UIDs_from_mepp:
    message = pyzmail.PyzMessage.factory(messages_from_me[UID][b'BODY[]'])
    torrent_URLs = re.findall('[^ ]+\.torrent',message.text_part.get_payload().decode(message.text_part.charset))

    # download each linked file with Transmission and send out a text notification
    for URL in torrent_URLs:
        subprocess.Popen(['transmission-gtk',URL])
        textMyself.textmyself(f'Started download of {URL}...')

    # delete the message so it doesn't get used next time
    imap_object.delete_messages(UID)

# log out of your email
imap_object.logout()
