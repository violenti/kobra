#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import socket
import dns.resolver
import dns.exception
import time
#import logging as log

filedns=''
resolver = dns.resolver.Resolver()
#resolver.nameservers=[socket.gethostbyname('8.8.8.8')]

def finddns(nameservers):
    for data in nameservers :
        print (data)

with open(filedns,encoding='utf-8') as f:
    for line in f:
        domain= line.strip()
        time.sleep(3)
        #nameservers = dns.resolver.query(domain, 'A')
        try:
            nameservers = dns.resolver.query(domain, 'A')
            finddns(nameservers)
        except dns.exception.DNSException as e:
            print ("not register")
            #log.info("instance not found: {}".format(repr(e)))

# for rdata in resolver.query('moni.com.ar', 'A'):
#     print (rdata)
