import chunk
from pickle import NONE
import sys
import os.path
from typing import List
import pandas as pd
CHUNKSIZE = 10000


class ArgumentException(Exception):
    "Raised when there are an incompatible number of arguments"
    pass


class BadFilePathException(Exception):
    "Raised when a specified file cannot be located"
    pass


def validateInput(args: List[str]) -> List[str]:
    '''Takes a list of arguments and validates it against requirements.
    Program must be called with >=  1 arguments from command line
     and each argument should be the path of a CSV file as str'''
    # try:
    if len(args) == 1:
        raise ArgumentException("Too few arguments. Expected >= 1")
    cleaned = args[1:]
    for filename in cleaned:
        if not os.path.isfile(filename):
            raise BadFilePathException("Couldn't find file " + filename)
        if len(filename) > 4 and filename[-4:] != ".csv":
            raise TypeError("File" + filename +
                            "does not appear to be a csv")

    return cleaned


def getFileName(s: str) -> str:
    '''Extracts the filename from the string representing its relative path'''
    position = len(s)-1
    while position >= 0 and s[position] != '\\' and s[position] != '/':
        position -= 1
    return s[position+1:]


def yieldChunk(files: List[str]) -> pd.DataFrame:
    '''Yields a chunk of size <= 10000 rows. Yields None
    when there are no files left to read'''
    for f in files:
        name = getFileName(f)
        chunks = pd.read_csv(f, chunksize=CHUNKSIZE)
        for chunk in chunks:
            chunk['filename'] = name
            yield chunk
    yield None


def main():
    '''Reads filenames from sys.argv and combines them into a single csv
    if they exist and have a .csv extension'''
    files = validateInput(sys.argv)
    for chunk in yieldChunk(files):
        if chunk is None:
            break
        chunk.to_csv(sys.stdout, mode="a", index = False)
            

if __name__ == "__main__":
    main()
