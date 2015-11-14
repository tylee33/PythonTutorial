# coding=utf-8

import ntplib
from time import ctime

def print_time():
    ntp_client = ntplib.NTPClient()
    response = ntp_client.request('202.120.2.101')
    print ctime(response.tx_time)

if __name__ == '__main__':
    print_time()
