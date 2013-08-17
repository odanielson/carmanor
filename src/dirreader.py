
import os

from twisted.internet import reactor

import config
from handler import Handler
from filereader import FileReader
from autotimeparser import AutoTimeParser


class DirReader(Handler):
    """Scans a directory recursively and creates a FileReader
    for every file found.

    NOTE: currently, directories and files are only detected
    at start.
    """
    def __init__(self, source_name, path, dest=[]):
        Handler.__init__(self, dest=dest)
        self.childrens = []
        self.name = source_name

        for f in os.listdir(path):
            if os.path.isfile("%s/%s" % (path, f)):
                self.childrens.append(
                    FileReader(f, "%s/%s" % (path, f), dest = dest))
            else:
                self.childrens.append(
                    DirReader(f, "%s/%s" % (path, f), dest))
