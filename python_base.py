
import os
import sys
import logging


def get_help_str():
    help_str = "incomplete."
    help_str += ""
    return help_str

def main():

    args = sys.argv
    help_str = get_help_str()
    opt = ["1"]
    if args[-1] not in opt:
        print(help_str)
        sys.exit(0)
    else:
        print(help_str)
        return None
    return None

if __name__ == "__main__":
    main()
