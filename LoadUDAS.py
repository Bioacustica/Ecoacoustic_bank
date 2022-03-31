#!/usr/local/bin/python3

import argparse
from LoadData import LoadData

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--UDAS', type = str, 
                    help = 'Path UDAS file')


args = parser.parse_args()

print(args.UDAS)

session = Session(engine)

