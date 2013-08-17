
import time

from twisted.python import log

import config


class Handler:
    """Baseclass for handling events.

    The idea with this class is to create a chain of event handlers,
    where each link in the chain (a subclass of Handler) makes something
    with an event and then forwards it to the next link in the chain.
    """

    def __init__(self, name="unknown", dest=[]):
        self.dest = dest
        self.name = name
        self.log_debug = True

    def debug(self, msg):
        if config.debug:
            log.msg("%s:DEBUG - %s" % (self.name, msg))

    def info(self, msg):
        log.msg("%s:INFO - %s" % (self.name, msg))

    def warning(self, msg):
        log.msg("%s:WARN - %s" % (self.name, msg))

    def push(self, msg):
        """Push event to all destination handlers.

        Override this function in your derrived classes but remember
        to call the base class in order to push the event forward."""
        for d in self.dest:
            d.push(msg)
