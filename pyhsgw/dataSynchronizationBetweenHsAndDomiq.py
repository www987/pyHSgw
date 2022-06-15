from shlex import join
import telnetlib
import sys
import datetime
import pathlib
import time
from time import sleep
from turtle import delay
from hsgw import HomeserverConnection

#conn = HomeserverConnection()
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
list_of_items_only_HS = []
domiqValueIndex = "list which collects only HS properties from domiq"
index = "created to store the domiq line index"
indexProblem = "created to store index if they are more searches"

# That function change domiq format (VAR.) to HS format
def changeToHsFormatAndCompare(domiqPresentPosition, domiqArchivePosition):
    domiqPresentPosition = domiqPresentPosition[4:].split("=")
    print(domiqPresentPosition[1], domiqArchivePosition[1], type(domiqPresentPosition[1]), type(domiqArchivePosition[1]), domiqPresentPosition[1] != domiqArchivePosition[1])
    if domiqPresentPosition[1] != domiqArchivePosition[1].rstrip("\n"):
        return str(domiqPresentPosition[0]+"    " + domiqPresentPosition[1] + " 1")
    else:
        return str(domiqPresentPosition[0]+"    " + domiqPresentPosition[1] + "    0")

while 1:
    """with open(pathHS, "r") as fileHs:
        f_hs = fileHs.readlines()
        linesAmount = len(f_hs)
        presentDate = datetime.datetime.now()
        while i<linesAmount:
            time.sleep(0.2)
            l_line = f_hs[i].split("\t")
            if l_line[6] == "1":
                conn.setValue(l_line[1],l_line[2])
                l_line[6] = 0
                f_hs[i] = "\t".join(str(item) for item in l_line)
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
    i = 0"""
    with telnetlib.Telnet(host, port, timeout) as session:
        with open(pathDomiq, "r") as fileDomiq:
            l_domiqDifference = []
            f_domiq = fileDomiq.readlines()
            linesAmount = len(f_domiq)
            presentDate = datetime.datetime.now()
            session.write(b"?\r\n")
            variables =session.read_until(b"<",timeout=7).decode("utf-8")
            list_of_items = []
            list_of_items_only_HS = []
            for l,item in enumerate(variables.splitlines()):
                list_of_items.append(item)
                print(l, item)
            while i<linesAmount:
                time.sleep(0.2)
                l_line = f_domiq[i].split("\t")
                index = [l for l,s in enumerate(list_of_items) if l_line[0] in s]
                if len(index) == 1:
                    list_of_items_only_HS.append(changeToHsFormatAndCompare(list_of_items[index[0]], l_line))
                    
                if len(index) > 1:
                    for k in index:
                        if list_of_items[k].startswith("VAR."+l_line[0]+"="):
                            list_of_items_only_HS.append(changeToHsFormatAndCompare(list_of_items[k], l_line))
                i+=1
            print(list_of_items_only_HS)
                
    break
        

"""
    Deleting VAR.VAR values
"""