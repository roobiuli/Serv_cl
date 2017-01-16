#!/usr/bin/python
import os
#cmd = raw_input("Please input ls command")

data = os.listdir('.')
stringData = ','.join(data)

print stringData