#!/usr/bin/python

from numpy import *
import sys
import scipy
import os

try:
    input_file  = sys.argv[1]
    output_dir = sys.argv[2]
except:
    print 'wrong parameters'
    print 'usage: %s input_file output_dir [first_frame] [last_frame]' % sys.argv[0]
    sys.exit(0)





f = open(input_file)
dim = frombuffer(f.read(8),int,2)
w = dim[0]; h = dim[1]
imsize = w*h*3
size = os.path.getsize(input_file)
nframes = size / imsize
print 'dimensions: %i, %i, number of frames: %i' % (w, h, nframes)

try:
    first = int(sys.argv[3])
    last = int(sys.argv[4])
except:
    first = 0
    last = nframes-1
print 'first frame: %i, last frame: %i' % (first, last)



f.seek(8+imsize*first)
for i in range(last-first+1):
    s = f.read(w*h*3)
    data = frombuffer(s,uint8)
    data = data.reshape((h,w,3))

    number = '00000000000%i' % (first+i)
    number = number[len(number)-len(str(last)):]

    out = "%s/%s.jpg" % (output_dir,number)
    scipy.misc.imsave(out,data)
    print out

f.close()

