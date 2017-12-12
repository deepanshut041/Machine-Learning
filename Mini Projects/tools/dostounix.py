#!/usr/bin/env python
"""
convert dos linefeeds (crlf) to unix (lf)
usage: dos2unix.py 
"""
original = "python2_lesson14_keys.pkl"
destination = "python2_lesson14_keys_unix.pkl"

content = ''
outsize = 0
with open(original, 'rb') as infile:
	content = infile.read()
with open(destination, 'wb') as output:
	for line in content.splitlines():
		outsize += len(line) + 1
		output.write(line + str.encode('\n'))
print("Done. Saved %s bytes." % (len(content)-outsize))