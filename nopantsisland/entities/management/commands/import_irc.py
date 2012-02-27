from django.core.management.base import BaseCommand, CommandError
from nopantsisland.entities.models import IrcLog
import re
from datetime import datetime
import time

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    logfile = 'irc.log'
    
    # save some cycles and compile the regex only once
    p = re.compile(r'^\[([^\]]*)\] (\S+) (.*)')

    def handle(self, *args, **options):
        f = open(self.logfile, 'r')
        x = []

        for line in f:
            data = self.parse_line(line)
            data_packet = {'type': data['type'], 'message': data['msg']}
            if data['type'] == 'message':
                data_packet['nick'] = data['nick']
            x = IrcLog(created_on=data['time'], entity_type="irc", data=data_packet).save();
            print "Saved %s" % data['type']

    def parse_line(self, line):

        # match our line
        m = self.p.match(line)

        # instantiate a placeholder data packet
        data = {}
        data['time'] = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S %Z") # parse our timestamp
        data['msg'] = m.group(3) # our message
        
        # and determine whether this is a command message or a real message
        if m.group(2) == "*":
            data['type'] = 'notice'
        else:
            data['type'] = 'message'
            data['nick'] = m.group(2)[1:-1] # nifty one liner to scoop the nickname out of the <>'s
                
        return data
