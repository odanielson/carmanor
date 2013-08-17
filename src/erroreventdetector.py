
from handler import Handler

class ErrorEventDetector(Handler):

    def __init__(self, dest=[]):
        Handler.__init__(self, dest=dest)
        self.match = False

    def push(self, data):

        match = data['raw'].find("ERROR")>=0
        if not self.match and match:
            self.info("Detected ERROR")
            data['type'] = 'event'
            data['raw'] = "@type:\"line\" AND @timestamp:[\"%s\" *] - %s" % (
                data['timestamp'], data['raw'])

            Handler.push(self, data)

        self.match = match
