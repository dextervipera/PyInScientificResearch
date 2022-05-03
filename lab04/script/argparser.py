#argparser 
import sys
from pathlib import Path

sys.path.insert(0,str(Path.cwd().parent)+'\modules')

import argparse
def parse():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('int1', type=int, help='liczba nr 1')
    parser.add_argument('int2', type=int, help='liczba nr 3')
    parser.add_argument('-n', '--name', type=str, help='nazwa')

    return parser.parse_args()

if __name__ == "__main__":
    args=parse()
    print(vars(args))

#print(args.accumulate(args.integers))
