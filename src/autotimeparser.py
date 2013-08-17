
import time
import pdb

from handler import Handler

#TODO: This class is currently not source independent,
#      we better fix it so that it handler the autodetection per source
#      attribute

class AutoTimeParser(Handler):
    """Tries to parse the timestamp in an event automatically."""

    def __init__(self, dest=[]):
        Handler.__init__(self, dest=dest)
        self.last_stamp = 0.0
        self.parser = self._autodetect
        self.parsers = { "stdtime": self._parse_std_time,
                         "spec1": self._parse_spec1_time,
                         "vsftpd": self._parse_vsftpd_time }

    def _format_time(self, stamp):
        return time.strftime("%Y-%m-%dT%H:%M:%S+00:00", time.gmtime(stamp))

    def _adjust_time(self, stamp):
        if stamp > self.last_stamp:
            self.last_stamp = stamp
        else:
            self.last_stamp = self.last_stamp + 0.001
        return self.last_stamp

    def _parse_std_time(self, data):

        t_s=time.gmtime(time.time())
        t=map(lambda x: int(x), data[7:15].split(":"))
        new_time = [ t_s[0], t_s[1], t_s[2], t[0], t[1],
                         t[2], t_s[6], t_s[7], t_s[8] ]

        return time.mktime(map(lambda x: int(x), new_time))

    def _parse_spec1_time(self, data):
        """ Parses time formatted as 2013-01-31 04:24:13+0100
        return epoch or raises ValueError exception """
        return time.mktime(time.strptime(data[0:19], "%Y-%m-%d %H:%M:%S"))

    def _parse_vsftpd_time(self, data):
        """ Parses time in format Wed Jan 30 18:14:03 2013   (vsftpd)
        returns epoch or raises ValueError Exception
        """
        return time.mktime(time.strptime(data[4:24], "%b %d %H:%M:%S %Y"))

    def _autodetect(self, data):
        for key, parser in self.parsers.iteritems():
            try:
                stamp = parser(data)
                self.parser = parser
                self.info("Detected %s timeformat" % (key))
                return stamp
            except ValueError as e:
                pass
        raise ValueError("Could parse time from %s" % (data))


    def push(self, data):
        self.debug("Parsing time in data %s" % (data))
        try:
            stamp = self.parser(data['raw'])
            stamp = self._format_time(self._adjust_time(stamp))
            data['timestamp'] = stamp
        except Exception as e:
            self.warning("Failed to parse time in %s" % (data['raw']))

        Handler.push(self, data)
