# parses an argument sequence and returns a sequence of tuples containing (option, argument) pairs.

# The getopt() function takes 3 argument:
#   1) sequence of arguments to be parsed, usually sys.argv[1]
#   2) option definition string for single-char options. 
#       If option requires an argument, its letter is followed by ":"
#   3)(optional) sequence of long option names. 
#       Should not include "--" prefix
#       If option requires an argument, its name should have a prefix of "="

import getopt
import sys

def short_option():
    opts, args = getopt.getopt(['-a', '-bval', '-c', 'val'], 'ab:c:')
    print getopt.getopt(['-a', '-bval', '-c', 'val'], 'ab:c:')
    # ([('-a', ''), ('-b', 'val'), ('-c', 'val')], []) 

def long_option():
    print getopt.getopt(['--noarg', '--witharg', 'val', '--witharg2=another'],
                        '',     # no short option, so empty string
                        ['noarg', 'witharg=', 'witharg2='])
    # ([('--noarg', ''), ('--witharg', 'val'), ('--witharg2', 'another')], [])


def comple_example(cmd_input):
    version = '1.0'
    verbose = False
    output_filename = 'default.out'

    try:
        options, remainder = getopt.getopt(cmd_input,
                                            'o:v',
                                            ['output=', 'verbose', 'version='])
    except getopt.GetoptError as err:
        print 'Error:', err
        sys.exit(1)

    for opt, arg in options:
        if opt in ('-o', '--output'):
            output_filename = arg
        elif opt in ('-v', '--verbose'):
            verbose = True
        elif opt == '--version':
            version = arg

    print 'Version: ', version
    print 'Verbose: ', verbose
    print 'Output: ', output_filename
    print 'Remaining: ', remainder


if __name__ == "__main__":
    comple_example(sys.argv[1:])


# Notes:
# 1) The long-form option does not have to be spelled out entirely, as long as a unique prefix is provided.
#    If a unique prefix is not provided, an exception is raised.
# ex: python Getopt.py --o foo  

# 2) Normally, option processing stops as soon as the first nonoption argument is encounted. 
#    An additional function gnu_getopt() allows option and nonoption arugment to be mixed in any order.

# 3) If getopt() encounter "--" in the input arguments, it stops processing the remaining arguments.




