import tweetstream
import pystache
import RPrinter.printer as rp
import time

printer = rp.RPrinter()

stream = tweetstream.FilterStream("login", "password", track=["columbo"])

template = """
**{{ timestamp }}**
**{{ screen_name }}**: {{ tweet }}
"""

for tweet in stream:
    if 'user' in tweet:

        # format date
        tweetDate = time.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")
        printDate = time.strftime("%b.%d %H:%M:%S", tweetDate)

        # setup context
        context = { 
            'timestamp': printDate, 
            'screen_name': tweet['user']['screen_name'].encode('ascii', 'ignore'),
            'tweet': tweet['text'].encode('ascii', 'ignore')
        }

        printer.printStr(pystache.render(template, context))