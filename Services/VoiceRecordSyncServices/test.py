# -*- coding: utf-8 -*-

from __future__ import absolute_import
from optparse import OptionParser
import time
import stomp


class SimpleListener(object):
    def on_error(self, headers, message):
        print '=> Received an error: %s' % message

    def on_message(self, headers, message):
        print '=> Received a message: %s' % message


def consume(options):
    connection = stomp.Connection(host_and_ports = [('localhost', 61613)])
    try:
        listener = SimpleListener()
        connection.set_listener('', listener)
        connection.start()
        connection.connect(wait = True)
        connection.subscribe(destination = options.destination, id = 1, ack = 'auto',
                             headers = {'selector': "flag='1'"})
        listener.wait_on_re

    finally:
        connection.disconnect()


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option(
        '--host',
        dest = 'host',
        default = 'localhost',
        help = 'Queue server host (defaults to localhost)',
        metavar = 'HOST')
    parser.add_option(
        '--port',
        dest = 'port',
        default = 61613,
        type = 'int',
        help = 'Queue server host (defaults to 61613)',
        metavar = 'POST')
    parser.add_option(
        '--destination',
        dest = 'destination',
        default = '/queue/whatever',
        help = 'Destination name (defaults to /queue/whatever)',
        metavar = 'QUEUE NAME')

    (options, args) = parser.parse_args()
    consume(options)