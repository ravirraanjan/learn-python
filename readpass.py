#!/usr/bin/python3

f = open('/etc/passwd', 'r')
count = 0

for lines in f:
    count += 1
    if not lines.startswith("#"):
       line = lines.split(":")
       print(line[0])
f.close()
