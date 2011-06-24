import os
from subprocess import call
from time import sleep
import sys

def main(args):

    if sys.argv[1] == 'commit' or sys.argv[1] == 'ci':
        print "Waiting 10 seconds in case of accidental checkin oops"
        sleep(10)

        # execute the tests
        command_path = os.path.join(args['bin'], args['command'])
        command = command_path + ' test '
        command += ' '.join([app + ' ' for app in args['apps']])
        result = call(command, shell = True)

        if result == 0:
            # now we can check in
            print "Tests passed, commencing checkin"
            call(['svn'] + sys.argv[1:])
        else:
            print "Your tests have failed, not checking in"
    else:
        call(['svn'] + sys.argv[1:])
