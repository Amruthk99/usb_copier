import os
import time
from distutils.dir_util import copy_tree

def checkAndCopy():
    src = 'D:\\'
    statement = os.path.exists(src) 
    if  statement:
        dst = "C:\\Users\Amruth Kuntamalla\Documents\sample"
        copy_tree(src, dst)
    
def main():
    checkAndCopy()
    
if __name__ == "__main__":
    main()
