import sys
from hsgw import HomeserverConnection

conn = HomeserverConnection()
value = conn.getValueByAddr("4/0/1")
print(value, value.decode("utf-8"))
#conn.setValue("4/0/1","1.0")


