#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import socket
import dns.resolver
import dns.exception
import time
import argparse
import sys

resolver = dns.resolver.Resolver()

##function for arguments
def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -i mydomain.txt")
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-i', '--input', help="file from will your list with domain",type=str, required=True)
    parser.add_argument('-o', '--output', help="file when writing the output",type=str,required=False)

    return parser.parse_args()

args = parse_args()

def finddns(nameservers, domain):
    output = args.output
    if output is None :
        for data in nameservers :
          print (domain,"",data)
    else:
        for data in nameservers:
           with open(output,"w",encoding='utf-8') as out:
               out.write('%s '%domain)
               out.write('%s'%"")
               out.write('%s \n'%data)


def main():
    #args = parse_args()
    filedns = args.input
    output = args.output
    with open(filedns,encoding='utf-8') as f:
       for line in f:
          domain= line.strip()
          time.sleep(3)
          try:
            nameservers = dns.resolver.query(domain, 'A')
            finddns(nameservers,domain)
          except dns.exception.DNSException as e:
               print (domain,"","not register")

if __name__ == '__main__':
    main()
