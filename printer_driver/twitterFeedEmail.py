from imaplib import *
from email.Parser import Parser
import datetime, time, email, email.Utils
import re
 
print "Hello"


# Connect to email server
server = IMAP4_SSL("imap.gmail.com")
server.login("rpi1@flimshaw.net", "NPInpi123")
r = server.select("inbox")
 
# Find only new mail (i.e. new direct messages)
r, data = server.uid('search', None, 'ALL')

print "Logged in"

# If there are new direct messages:
if len(data[0]) > 0:
 
    p = Parser()
 
    # Loop through new emails
    for uid in data[0].split():
 
        r, fetch_data = server.uid('fetch', uid, '(BODY[HEADER.FIELDS (DATE SUBJECT FROM X-TwitterEmailType X-TwitterSenderScreenName X-TwitterCreatedAt X-TwitterRecipientScreenName)])')
        msg = p.parsestr(fetch_data[0][1])
        who = msg.__getitem__('X-TwitterEmailType')
        print who

# Logout of email server
server.logout()