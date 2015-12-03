
import sys
import getopt
import time
from os import popen
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import sendp, IP, UDP, Ether, TCP
from random import randrange


def sourceIPgen():
    not_valid = [10,127,254,1,2,169,172,192]

    first = randrange(1,256)

    while first in not_valid:
        first = randrange(1,256)

    ip = ".".join([str(first),str(randrange(1,256)),str(randrange(1,256)),str(randrange(1,256))])

    return ip


def gendest(start, end):

    first = 10
    second =0; third =0;
    ip = ".".join([str(first),str(second),str(third),str(randrange(start,end))])
   # print start
   # print end
    return ip

#if __name__ == '__main__':
  #main()

def main(argv):
   # global start 
   # global end
    print argv
    try:
        opts, args = getopt.getopt(sys.argv[1:],'s:e:',['start=','end='])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt =='-s':
            start = int(arg)
        elif opt =='-e':
            end = int(arg)
    if start == '':
        sys.exit()
    if end == '':
        sys.exit()


    interface = popen('ifconfig | awk \'/eth0/ {print $1}\'').read()

    for i in xrange(1000):
        packets = Ether()/IP(dst=gendest(start, end),src=sourceIPgen())/UDP(dport=80,sport=2)
        print(repr(packets))

        sendp( packets,iface=interface.rstrip(),inter=0.1)

if __name__ == '__main__':
  main(sys.argv)


