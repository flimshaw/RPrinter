import tweetstream
import RPrinter.printer as rp
import time

printer = rp.RPrinter()

print "TwitterFeed!"

stream = tweetstream.FilterStream("NPIDevice1", "NPInpi123", track=["columbo"])

for tweet in stream:
    print "Tweet Received!"
    print tweet
    if 'user' in tweet:
        tweetDate = time.strptime(tweet['created_at'], "%a %b %d %H:%M:%S +0000 %Y")
        printer.println(time.strftime("%b.%d %H:%M:%S", tweetDate))
        printer.toggleMode(8)
        printer.printChar("@%s:\n" % (tweet['user']['screen_name'].encode("ascii", "ignore")))
        printer.toggleMode(8)
        printer.printChar(tweet['text'].encode("ascii", "ignore"))
        printer.printChar("\n\n")
        time.sleep(1)