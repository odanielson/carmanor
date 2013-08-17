
from handler import Handler


class StdoutPrinter(Handler):
    """Log events on std output."""
    def __init__(self, dest=[]):
        Handler.__init__(self, dest=dest)

    def push(self, data):
        if (data.has_key('timestamp')):
            print("%s - %s : %s" % (data['timestamp'],
                                    data['source'],
                                    data['raw']))
        else:
            print("unknown - %s : %s" % (data['source'],
                                         data['raw']))

        Handler.push(self, data)
