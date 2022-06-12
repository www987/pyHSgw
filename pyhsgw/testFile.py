import pathlib
import datetime
from hsgw import HomeserverConnection

pathHS = pathlib.Path.cwd() / "fHSParameters.txt"
f_hs = "a"
conn = HomeserverConnection()
listTest = []
i=0
with open(pathHS, "r") as fileHs:
    f_hs = fileHs.readlines()
    #print(f_hs, type(f_hs))
    linesAmount = len(f_hs)
    while i<linesAmount:
        l_line = f_hs[i].split("\t")
        valuePlaceholder = conn.getValueByAddr(l_line[1])
        print("z",l_line[1],"z")
        listTest.append(str(l_line[0]) + "  " + str(l_line[1]) + "   " + valuePlaceholder.decode("utf-8"))
        i+=1
print(listTest)
print("aa", "sss", "gg")
presentDate = datetime.datetime.now()
print()
