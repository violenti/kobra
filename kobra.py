#!/usr/bin/python3
# -*- coding: UTF-8 -*-
"""System module."""

import time
import argparse
import sys
import dns.resolver
import dns.exception

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

def parse_args():
    """
    function for argparse

    """
    parser = argparse.ArgumentParser(epilog='\tExample:\r\npython'
                                     + sys.argv[0] +
                                     "-i mydomain.txt")
    parser._optionals.title = "OPTIONS"
    parser.add_argument('-i', '--input', help="file from will your list with domain",
                       type=str, required=True)
    parser.add_argument('-r','--resolver',
                        help="dns name for resolver,for example 8.8.8.8",
                        type=str, required=False)
    parser.add_argument('-t','--type',help="type of dns record for finding",
                        type=str,required=False)

    return parser.parse_args()

args = parse_args()

def finddns(nameservers, domain):
    """
    function of support
    """

    for data in nameservers :
        print (domain,"",data)


def main():
    """
    function main
    """
    filedns = args.input
    #output = args.output
    resolverdns = args.resolver
    typerecords = args.type
    nameservers= ''
    if typerecords is None:
        print ("Please set the dns records")
    else:
        with open(filedns,encoding='utf-8') as file:
            for line in file:
                domain= line.strip()
                time.sleep(3)
                if resolverdns is None:
                    try:
                        nameservers = dns.resolver.Resolver(domain, typerecords)
                    except dns.exception.DNSException:
                        print (domain,"","not register")
                else:
                    resolver=dns.resolver.Resolver(configure=False)
                    resolver.nameservers = [resolverdns]
                    try:
                        nameservers = dns.resolver.Resolver(domain,typerecords)
                    except dns.exception.DNSException:
                        print (domain,"","not register")
                finddns(nameservers,domain)


if __name__ == '__main__':
    main()
