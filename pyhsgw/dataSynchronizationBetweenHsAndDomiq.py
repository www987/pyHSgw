from shlex import join
import sys
import datetime
import pathlib
import time
from time import sleep
from turtle import delay
from hsgw import HomeserverConnection

conn = HomeserverConnection()

#Variables used in program
f_hs = "Object with lines from fHSParameters.txt"
f_domiq = "Object with lines from fCheckChangeDomiq.txt"
linesAmount = 0
i = 0
l_line = "every line from files"
valuePlaceholder = 0
presentDate = "datetime.datetime.now()"
pathHS = pathlib.Path.cwd() / "fHSParameters.txt"
pathDomiq = pathlib.Path.cwd() / "fCheckChangeDomiq.txt"

while 1:
    with open(pathHS, "r") as fileHs:
        f_hs = fileHs.readlines()
        linesAmount = len(f_hs)
        presentDate = datetime.datetime.now()
        while i<linesAmount:
            time.sleep(0.2)
            l_line = f_hs[i].split("\t")
            if l_line[6] == "1":
                #conn.setValue(l_line[1],l_line[2])
                l_line[6] = 0
                f_hs[i] = ''.join(l_line.decode("utf-8"))
            else:
                valuePlaceholder = conn.getValueByAddr(l_line[1]).decode("utf-8")
                print(valuePlaceholder, l_line[1])
                if valuePlaceholder != l_line[2]:
                    l_line[2] = valuePlaceholder
                    l_line[3] = presentDate.strftime("%Y:%m:%d %H:%M:%S")
                    l_line[5] = 1
                    f_hs[i] = "\t".join(str(item) for item in l_line)
            i+=1
    with open(pathHS, "w") as fileHs:
        fileHs.write("".join(str(item) for item in f_hs))
    time.sleep(3.2)
    i = 0