#!/usr/bin/python -tt

# record and read a tty session for further use.

import sys, subprocess

def read():
    fname = raw_input("Name the file you want to read : ")
    with open(str(fname)+'.ter', 'rU') as typescript:
        print typescript.read()


def main ():
    if len(sys.argv) != 2 or sys.argv[1] not in ['--rec', '--read']:
        print """Usage : 
        \n \t terms.py --rec    : To record a session
         terms.py --read   : To read a session \n\n"""

    if len(sys.argv) == 2:
        if sys.argv[1] == '--rec':
            print "Record mode started"
            fname = raw_input("Name this file : ")
            subprocess.call("script -q", shell=True)
            subprocess.call('mv typescript ' + str(fname) + '.ter', shell=True)

        if sys.argv[1] == '--read':
            read()

if __name__ == '__main__':
    main()
