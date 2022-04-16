#charcodes

import locale
locale.getpreferredencoding()

def char():
    pass
    
if __name__=="__main__":
    print("main")
    print(chr(176))
    
    all(len(chr(i).encode("ascii")) == 1 for i in range(128))
    print(all)
