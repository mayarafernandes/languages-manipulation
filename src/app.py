import sys, getopt
from operations import *

def main():
    try:
        opts, _ = getopt.getopt(sys.argv[1:],"l:c:",["list=", "convert="])
        if opts[0][0] == '-l':
            list_data(opts[0][1])
    except getopt.GetoptError:
        print ('app.py -l <type>')
        sys.exit(2)

if __name__ == "__main__":
   main()
