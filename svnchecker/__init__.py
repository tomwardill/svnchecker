import os
from subprocess import call


def main(args):
    print args

    # execute the tests
    command_path = os.path.join(args['bin'], args['command'])
    command = command_path + ' test '
    command += ' '.join([app + ' ' for app in args['apps']])
    result = call(command, shell = True)

    if result == 0:
        print "pass"
    else:
        print "fail"
