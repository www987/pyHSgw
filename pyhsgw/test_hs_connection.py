#!/usr/bin/python

import sys
from hsgw import HomeserverConnection

conn = HomeserverConnection(key=sys.argv[1])
print("Sun - lux: ", conn.getValueByAddr("4/4/0"))
conn.setValue("0/0/1","0.0")
