#importing
import sys
from pathlib import Path

#sys.path.insert(0,"e:\PyPhd\lab04\modules")
sys.path.insert(0,str(Path.cwd().parent)+'\modules')

import fun1


if __name__ == "__main__":
    print(sys.argv)
    res = fun1.smlt(*sys.argv[1:])
    print(res)
    
    print("xxx")

