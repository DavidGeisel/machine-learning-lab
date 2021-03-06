"""Collection of file writers."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os


class LinewiseCSVWriter:
    def __init__(self, filename, header=None, sync=True, append=False):
        """CSV Writer which writes a single line at a time, and by default syncs to disk after every line.
        This is useful for eg. log files, where you want progress to appear in the file as it happens (instead of being written to disk when python exists)
        Data should be passed to the writer as an iterable, as conversion to string and so on is done within the class.
        Keyword arguments:
        filename -- the csv file to write to
        header (default: None) -- An iterator (eg. list) containing an optional CSV header, which is written as the first line of the file.
        sync (default: True) -- Flush and sync the output to disk after every write operation. This means data appears in the file instantly instead of being buffered
        append (default: False) -- Append to an existing CSV file. By default, the csv file is overwritten each time.
        """
        self.autoflush = sync
        self.len = None

        mode = 'a' if append else 'w'
        self.f = open(filename, mode)

        if header:
            self.write(header)

    def __del__(self):
        self.flush()
        self.f.close()

    def write(self, data):
        """Write a line of data to the csv file - data should be an iterable."""
        if self.len is None:
            self.len = len(data)
        assert len(data) == self.len, 'Length of passed data does not match previous rows'

        text = '"' + '","'.join([str(x).replace('"', '""') for x in data]) + '"\n'

        self.f.write(text)
        if self.autoflush:
            self.flush()

    def flush(self):
        """Manually flush the csv. Useless if flush=True in the class, as this is called after every write anyway."""
        self.f.flush()
        os.fsync(self.f.fileno())
