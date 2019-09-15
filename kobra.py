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
    parser.add_argument('-r','--resolver',help="dns name for resolver, for example 8.8.8.8", type=str, required=False)
    return parser.parse_args()

args = parse_args()

##print domains
def finddns(nameservers, domain):
    for data in nameservers :
        print (domain,"",data)

def main():
    filedns = args.input
    output = args.output
    resolverdns = args.resolver
    with open(filedns,encoding='utf-8') as f:
       for line in f:
          domain= line.strip()
          time.sleep(3)
          if resolverdns is None:
           try:
             nameservers = dns.resolver.query(domain, 'A')
           except dns.exception.DNSException as e:
               print (domain,"","not register")
          else:
              resolver=dns.resolver.Resolver(configure=False)
              resolver.nameservers = [resolverdns]
              print (resolver.nameservers)
              try:
                nameservers = dns.resolver.query(domain, 'A',)
              except dns.exception.DNSException as e:
                   print (domain,"","not register")

          if output is None:
              finddns(nameservers,domain)

          else:
              finddnsoutput(domain,nameservers,output)


if __name__ == '__main__':
    main()
