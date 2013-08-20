
import time

from twisted.internet import reactor

import config
from handler import Handler


class FileReader(Handler):
    """Scans a file and pushes each line as en event forward in the chain."""

    def __init__(self, source_name, filename, dest=[]):
        Handler.__init__(self, dest=dest)
        self.info("Initializing filereader at %s" % (filename))

        self.name = source_name
        self.count = 0
        self.last_report = time.time()

        self.file = open(filename)
        self.read()
        self.report()

    def report(self):
        current = time.time()
        dt = current - self.last_report
        self.info("Logged %d entries in %f seconds." % (self.count, dt))
        self.count = 0
        self.last_report = current
        reactor.callLater(config.report_interval, self.report)

    def read(self):
        line = self.file.readline()
        while line:
            self.count += 1
            Handler.push(self, {'type': 'line',
                                'raw': line.strip(),
                                'source': self.name })
            line = self.file.readline()
        reactor.callLater(1, self.read)
