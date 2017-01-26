import re
txt=open("proj2.txt").read();

print ''.join(re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',txt))

