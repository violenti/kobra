#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import socket
import dns.resolver
import dns.exception
import time
import argparse
import sys

#filedns='moni.txt'
resolver = dns.resolver.Resolver()
#resolver.nameservers=[socket.gethostbyname('8.8.8.8')]

##function for arguments
def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -i mydomain.txt")
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-i', '--input', help="file from will your list with domain", required=True)

    return parser.parse_args()

def finddns(nameservers, domain):
    for data in nameservers :
        print (domain,"",data)

def main():
    args = parse_args()
    filedns = args.input
    with open(filedns,encoding='utf-8') as f:
       for line in f:
          domain= line.strip()
          time.sleep(3)
          #nameservers = dns.resolver.query(domain, 'A')
          try:
            nameservers = dns.resolver.query(domain, 'A')
            finddns(nameservers,domain)
          except dns.exception.DNSException as e:
               print (domain,"","not register")
            #log.info("instance not found: {}".format(repr(e)))

if __name__ == '__main__':
    main()
