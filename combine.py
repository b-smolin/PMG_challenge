import sys
import os.path
from typing import List
# import pandas as pd


class ArgumentException(Exception):
    "Raised when there are an incompatible number of arguments"
    pass


def validateInput(args: List[str]) -> List[str]:
    '''Takes a list of arguments and validates it against requirements.
    Program must be called with >=  1 arguments from command line
     and each argument should be the path of a CSV file as str'''
    try:
        if len(args) == 1:
            raise ArgumentException("Too few arguments. Expected >= 1")
        cleaned = args[1:]
        for filename in cleaned:
            if not os.path.isfile(filename):
                raise IOError("Couldn't find file " + filename)
            if len(filename) > 4 and filename[-4:] != ".csv":
                raise TypeError("File" + filename +
                                "does not appear to be a csv")

        return cleaned

    except (ArgumentException, IOError, TypeError) as e:
        print(e)
        sys.exit(2)


def getFileName(s: str) -> str:
    '''Extracts the filename from the string representing its relative path'''
    position = len(s)-1
    while position >= 0 and s[position] != '\\':
        position -= 1
    return s[position+1:]


def main():
    files = validateInput(sys.argv)
    for f in files:
        print(getFileName(f))


if __name__ == "__main__":
    main()
