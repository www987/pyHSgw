import sys
from hsgw import HomeserverConnection

conn = HomeserverConnection()
#conn.setValue("0/2/0",0)
value = conn.getValueByAddr("4/4/0")
print(value)



