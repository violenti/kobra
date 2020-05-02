#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import socket
import dns.resolver
import dns.exception
import time
import argparse
import sys

resolver = dns.resolver.Resolver()
print (r"""
  _         _
 | |       | |
 | | _____ | |__  _ __ __ _
 | |/ / _ \| '_ \| '__/ _` |
 |   < (_) | |_) | | | (_| |
 |_|\_\___/|_.__/|_|  \__,_|

  by @violenti https://github.com/violenti/kobra
  LICENSE MIT
     """)

##function for arguments
def parse_args():
    # parse the arguments
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -i mydomain.txt")
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-i', '--input', help="file from will your list with domain",type=str, required=True)
    #parser.add_argument('-o', '--output', help="file when writing the output",type=str,required=False)
    parser.add_argument('-r','--resolver',help="dns name for resolver, for example 8.8.8.8", type=str, required=False)
    parser.add_argument('-t','--type',help="type of dns record for finding", type=str,required=False)
    return parser.parse_args()

args = parse_args()

##print domains
def finddns(nameservers, domain):
    for data in nameservers :
        print (domain,"",data)


def main(): #va a recibir un tipo de records y un dns
    filedns = args.input # tiene que tener
    #output = args.output # no es necesario
    resolverdns = args.resolver # es necesario
    typerecords = args.type # es necesario
    nameservers= ''
    with open(filedns,encoding='utf-8') as f:
       for line in f:
          domain= line.strip()
          time.sleep(3)
          if resolverdns is None:
           try:
             nameservers = dns.resolver.query(domain, typerecords)
           except dns.exception.DNSException as e:
               print (domain,"","not register")
          else:
              resolver=dns.resolver.Resolver(configure=False)
              resolver.nameservers = [resolverdns]
              try:
                nameservers = dns.resolver.query(domain,typerecords)
              except dns.exception.DNSException as e:
                   print (domain,"","not register")

          finddns(nameservers,domain)


if __name__ == '__main__':
    main()
