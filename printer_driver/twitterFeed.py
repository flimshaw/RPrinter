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
r, data = server.uid('search', None, 'UnSeen')

print "Logged in"

# If there are new direct messages:
if len(data[0]) > 0:
 
    p = Parser()
 
    # Loop through new emails
    for uid in data[0].split():
 
        r, msg = server.uid('fetch', uid, '(RFC822)')
        print msg[0][1]
        
# Logout of email server
server.logout()