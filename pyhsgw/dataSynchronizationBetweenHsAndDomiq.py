from shlex import join
import telnetlib
import sys
import datetime
import pathlib
import time
from time import sleep
from turtle import delay

from pyparsing import line
from hsgw import HomeserverConnection


#connection Variables Domiq
host = "212.51.218.27"
port = 4224
timeout = 100

#Variables used in program with description
f_hs = "Object with lines from fHSParameters.txt"
f_domiq = "Object with lines from fCheckChangeDomiq.txt"
linesAmount = 0
i = 0
l_line = "every line from files"
valuePlaceholder = 0
presentDate = "datetime.datetime.now()"
pathHS = pathlib.Path.cwd() / "fHSParameters.txt"
pathDomiq = pathlib.Path.cwd() / "fCheckChangeDomiq.txt"
variables = "var which contains domiq properties"
list_of_items = "list which collects all properties from domiq"
list_of_items_only_Domiq_Changed = []
domiqValueIndex = "list which collects only HS properties from domiq"
index = "created to store the domiq line index"
indexProblem = "created to store index if they are more searches"
timeDelay = 10 # How ofthen you want to synchronize data
synchronizeSerie = 0
# That function change domiq format (VAR.) to HS format and takes current value
def changeToHsFormatAndCompare(domiqPresentPosition, domiqArchivePosition):
    domiqPresentPosition = domiqPresentPosition[4:].split("=")
    try:
        float(domiqArchivePosition[1].rstrip("\n"))
        domiqArchivePositionFloat = float(domiqArchivePosition[1].rstrip("\n"))
        domiqPresentPositionFloat = float(domiqPresentPosition[1].rstrip("\n"))
    except ValueError:
        domiqArchivePositionFloat = domiqArchivePosition[1].rstrip("\n")
        domiqPresentPositionFloat = domiqPresentPosition[1].rstrip("\n") 
    if domiqPresentPositionFloat != domiqArchivePositionFloat:
        list_of_items_only_Domiq_Changed.append(str(domiqPresentPosition[0]+"\t" + domiqPresentPosition[1])) # SEE THIS
        

while 1:
    conn = HomeserverConnection()
    with open(pathHS, "r") as fileHs:
        f_hs = fileHs.readlines()
        linesAmount = len(f_hs)
        presentDate = datetime.datetime.now()
        while i<linesAmount:
            time.sleep(0.2)
            l_line = f_hs[i].split("\t")
            if l_line[6].rstrip("\n") == "1":
                conn.setValue(l_line[1],l_line[2])
                l_line[5] = 0
                l_line[6] = "0\n"
                f_hs[i] = "\t".join(str(item) for item in l_line)
            else:
                valuePlaceholder = conn.getValueByAddr(l_line[1]).decode("utf-8")
                print(valuePlaceholder, l_line[1])
                if valuePlaceholder != l_line[2]:
                    l_line[2] = valuePlaceholder
                    l_line[3] = presentDate.strftime("%Y.%m.%d %H:%M:%S")
                    l_line[5] = 1
                    l_line[6] = "0\n"
                    f_hs[i] = "\t".join(str(item) for item in l_line)
            i+=1
    with open(pathHS, "w") as fileHs:
        fileHs.write("".join(str(item) for item in f_hs))
    time.sleep(3.2)
    i = 0
    with telnetlib.Telnet(host, port, timeout) as session:
        with open(pathDomiq, "r") as fileDomiq:
            f_domiq = fileDomiq.readlines()
            linesAmount = len(f_domiq)
            presentDate = datetime.datetime.now()
            session.write(b"?\r\n")
            variables =session.read_until(b"<",timeout=7).decode("utf-8")
            list_of_items = []
            list_of_items_only_Domiq_Changed = []
            for l,item in enumerate(variables.splitlines()):
                list_of_items.append(item)
                print(l, item)
            while i<linesAmount:
                time.sleep(0.2)
                l_line = f_domiq[i].split("\t")
                index = [l for l,s in enumerate(list_of_items) if l_line[0] in s]
                if len(index) == 1:
                    if list_of_items[index[0]].startswith("VAR."+l_line[0]+"="):
                        changeToHsFormatAndCompare(list_of_items[index[0]], l_line)
                if len(index) > 1:
                    for k in index:
                        if list_of_items[k].startswith("VAR."+l_line[0]+"="):
                            changeToHsFormatAndCompare(list_of_items[k], l_line)
                i+=1
            print(list_of_items_only_Domiq_Changed)
            print(f_domiq)
        i = 0
        with open(pathHS, "r") as fileHs:
            f_hs = fileHs.readlines()
            linesAmount = len(f_hs)
            presentDate = datetime.datetime.now()
            while i<linesAmount:
                if f_hs[i] != "\n":
                    time.sleep(0.2)
                    l_line = f_hs[i].split("\t")
                    if any(l_line[1] in elem for elem in list_of_items_only_Domiq_Changed):
                        index = [l for l,s in enumerate(list_of_items_only_Domiq_Changed) if s.startswith(l_line[1] + "\t")]
                        valuePlaceholder = list_of_items_only_Domiq_Changed[index[0]].split("\t")
                        l_line[2] = valuePlaceholder[1]
                        l_line[4] = presentDate.strftime("%Y.%m.%d %H:%M:%S")
                        l_line[5] = "0"
                        l_line[6] = "1\n"
                        f_hs[i] = "\t".join(str(item).rstrip("\t") for item in l_line)
                    else:
                        if l_line[5] == "1":
                            session.write(bytes("VAR."+l_line[1]+"="+l_line[2]+"\r\n", encoding='ascii'))
                            session.write(b"?\r\n")
                            l_line[5] = "0"
                            l_line[6] = "0\n"
                            f_hs[i] = "\t".join(str(item).rstrip("\t") for item in l_line)
                    i+=1
        session.read_until(b"<",timeout=3).decode("utf-8")
    i = 0
    with open(pathHS, "w") as fileHs:
        fileHs.write("".join(str(item) for item in f_hs))
    with open(pathDomiq, "w") as fileHs:
        while i< linesAmount:
            l_line = f_hs[i].split("\t")
            fileHs.write(l_line[1]+ "\t" + l_line[2]+"\n")
            i+=1
    i = 0
    synchronizeSerie+=1
    print("Repetition: "+ str(synchronizeSerie))
    del conn
    time.sleep(timeDelay)    
    
"""
    Deleting VAR.VAR values

    Remember that if you changed anything in domiq you need to do session.read_until(b"<",timeout=3).decode("utf-8") two times to see changes
"""