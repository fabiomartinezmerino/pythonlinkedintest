import os
from os import path
import argparse

def main():
    parser = argparse.ArgumentParser(
    prog='test6',
    description='Admit name of file')
    parser.add_argument('filename')
    args = parser.parse_args()
    mydict = vars(args)
    print(mydict)
    print(mydict["filename"])

    myfile = mydict["filename"]

    print (os.path.exists(myfile))
    print ((os.path.abspath(myfile)).split("\\"))



if "__name__" == "__main__":
    main()