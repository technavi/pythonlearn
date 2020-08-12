import os
from os import path
import datetime
from datetime import date,time,timedelta
import time

def main():
    print(os.name)
    print(str(path.exists("tdsf.txt")))
    print(str(path.realpath("tdsf.txt")))
    p=path.split(str(path.realpath("tdsf.txt")))
    for i in p:
        print(i)
    #get file modification time
    t=time.ctime(path.getmtime("tdsf.txt"))
    print(t)
main()


