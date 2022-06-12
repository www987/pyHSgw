import sys
from hsgw import HomeserverConnection

conn = HomeserverConnection()
print("Sun - lux: ", conn.getValueByAddr("4/4/0"))
conn.setValue("0/0/1","0.0")

