#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    numarg = len(sys.argv) - 1
    if numarg == 0:
	print("{:d} arguments.".format(numarg))
    elif numarg == 1:
	print("{:d} argument:".format(numarg))
    else:
        print("{:d} arguments.".format(numarg))
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        print("{:d}: {:s}".format(i, sys.argv[i]))
