from twisted.internet import reactor

import config
from handler import Handler


class FileReader(Handler):
    """Scans a file and pushes each line as en event forward in the chain."""

    def __init__(self, source_name, filename, dest=[]):
        Handler.__init__(self, dest=dest)
        self.info("Initializing filereader at %s" % (filename))

        self.name = source_name
        self.file = open(filename)
        self.read()

    def read(self):
        line = self.file.readline()
        while line:
            Handler.push(self, {'type': 'line',
                                'raw': line.strip(),
                                'source': self.name })
            line = self.file.readline()
        reactor.callLater(1, self.read)
