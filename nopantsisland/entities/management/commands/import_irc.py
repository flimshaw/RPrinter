from django.core.management.base import BaseCommand, CommandError
from nopantsisland.entities.models import User, Entity
import re
import time

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    logfile = '/Users/charlie/irc.log'

    def handle(self, *args, **options):
        f = open(self.logfile, 'r')
        x = []

        for line in f:
            l = self.parse_line(line)
            x.append(l)

        for j in x:
            print j

    def parse_line(self, line):
        # play by play:     datestamp  nick/* msg
        p = re.compile(r'^\[([^\]]*)\] (\S+) (.*)')
        m = p.match(line)
        data = {}
        data['time'] = time.strptime(m.group(1), "%Y-%m-%d %H:%M:%S %Z")
        data['msg'] = m.group(3)
        
        if m.group(2) == "*":
            data['type'] = 'notice'
        else:
            data['type'] = 'message'
            data['nick'] = m.group(2)[1:-1] # nifty one liner to scoop the nickname out of the <>'s
                
        return data
