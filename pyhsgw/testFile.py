import pathlib
import datetime
import telnetlib
from hsgw import HomeserverConnection

#connection Variables Domiq
host = "212.51.218.27"
port = 4224
timeout = 100

pathHS = pathlib.Path.cwd() / "fHSParameters.txt"
EmptyLins = pathlib.Path.cwd() / "EmptyLineTest.txt"
 
print(float("100.5"))
#session.write(b"VAR.2/0/2=20\r\n")
#session.write(b"?\r\n")
#session.write(b"VAR.0/2/0=125\r\n")
''' with telnetlib.Telnet(host, port, timeout) as session:
    session.write(b"VAR.0/2/0=20\r\n")
    
    variables =session.read_until(b"<",timeout=7).decode("utf-8")
    list_of_items = []
    list_of_items_only_Domiq_Changed = []
    for l,item in enumerate(variables.splitlines()):
        list_of_items.append(item)
        print(l, item) '''
if 0.00:
    print(0.00)
else:
    print("adam")
''' print(float("50.0")/2.5)

def makeFloatIfPossible(string):
    tempValue = 0.00
    try:
        tempValue = float(string)
    except ValueError:
        tempValue = string
    return tempValue
print(makeFloatIfPossible("aa")) '''

''' 
test = ["lama", "kota", "ma"]
vara = "\t".join(str(item) for item in test)
print(vara.rstrip("\t"),"a", vara, "a")
presentDate = datetime.datetime.now() '''



