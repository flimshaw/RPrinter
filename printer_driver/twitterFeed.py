import tweetstream
import printer as rp
import time

printer = rp.RPrinter()

print "TwitterFeed!"

stream = tweetstream.FilterStream("NPIDevice1", "NPInpi123", follow=[713566676])

for tweet in stream:
    print "Tweet Received!"
    tweetDate = time.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")
    printer.printChar(time.strftime("%b.%d %H:%M:%S\n\n", tweetDate))
    printer.toggleMode(8)
    printer.println("@%s: " % (tweet['user']['screen_name']))
    printer.toggleMode(8)
    printer.printStr(tweet['text'])
    printer.println("\n\n\n\n")