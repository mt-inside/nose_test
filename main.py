#!/usr/bin/env python

import sys

class Utils(object):
    def fib_iter(this,n):
        acc1 = 1
        acc2 = 1

        for i in range(1,n):
            tmp = acc2
            acc2 += acc1
            acc1 = tmp

        return acc2

def main(args=None):
    print args
    u = Utils()
    for i in range(0,10):
        print u.fib_iter(i)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
