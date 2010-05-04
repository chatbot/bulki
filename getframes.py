#!/usr/bin/python

from numpy import *
import sys
import scipy

try:
    input_file  = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    output_dir = sys.argv[4]
except:
    print 'wrong parameters'
    print 'usage: %s input_file startpos endpos output_dir' % sys.argv[0]
    sys.exit(0)




f = open(sys.argv[1])
dim = frombuffer(f.read(8),int,2)
w = dim[0]; h = dim[1]
print 'dimensions: %i, %i' % (w,h)


imsize = w*h*3
f.seek(8+imsize*start)
for i in range(end-start+1):
    s = f.read(w*h*3)
    data = frombuffer(s,uint8)
    data = data.reshape((h,w,3))

    out = "%s/%i.jpg" % (output_dir,start+i)
    print out
    scipy.misc.imsave(out,data)
