import sys
from hsgw import HomeserverConnection

conn = HomeserverConnection()
value = conn.getValueByAddr("4/1/0")
print(value, value.decode("utf-8"))



