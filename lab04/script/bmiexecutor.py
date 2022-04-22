#bmiexecutor
if __name__ == "__main__":
    import sys
    from pathlib import Path

    sys.path.insert(0,str(Path.cwd().parent)+'\modules')

    from fun1 import bmi
    print (bmi(*sys.argv[1:]))