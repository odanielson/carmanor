
import datetime
import socket

from pyelasticsearch import ElasticSearch

import config
from handler import Handler


class ElasticEvent(object):
    """Represents an event in a format suitable for pushing to ES."""

    def __init__(self, event):

        self.data = { "@message": event.get('raw'),
                      "@source": event.get('source'),
                      "@source_host": event.get('source_host') or self.host(),
                      "@source_path": event.get('source'),
                      "@timestamp": event.get('timestamp') or self.timestamp(),
                      "@type": event.get('type') }

    def timestamp(self):
        return datetime.datetime.now().strftime("%Y-%m-%dT%X.%fZ")

    def host(self):
        return socket.gethostname()

    def dict(self):
        return self.data


class ElasticPush(Handler):
    """Posts events to ES."""

    def __init__(self, host='localhost', dest=[]):
        Handler.__init__(self, dest=dest)
        self.es = ElasticSearch('http://%s:9200/' % (host))
        self.source_host = socket.gethostname()

    def push(self, data):
        self.debug("Pushing data %s to elastic search" % (data))
        event = ElasticEvent(data)
        self.es.index("carmanor", "line", event.dict())

        Handler.push(self, data)
