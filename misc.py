from numpy import *
from PIL import Image
import math

def list2m(l,xmax=None,ymax=None):
    xx = map(lambda (p): p[0],l)
    yy = map(lambda (p): p[1],l)
    xmax = max(xx)+1 if xmax == None else xmax
    ymax = max(yy)+1 if ymax == None else ymax
 #   print xmax,ymax
    m = zeros((xmax,ymax),int)
    for p in l:
        #print p[0],p[1]
        m[p[0]][p[1]]=1
    return m


def m2list(m):
    l = list()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                l.append((i,j))
    return l



def writematrix(l,name):
    
    m = list2m(l)
    strings = map(lambda (x): " ".join(map(str,x)), m)
    strings = ("\n").join(strings) + "\n"

    f = open(name,"w")
    f.write(strings)
    f.close()


def writelist(l, name):
    strings = map(lambda (x): str(x[0])+' '+str(x[1]), l)
    strings = ("\n").join(strings) + "\n"
    f = open(name,"w")
    f.write(strings)
    f.close()


def loadcontour(name):
    
    im = Image.open(name)
    ary = array(im.getdata())
    ary = ary.reshape((im.size[1],im.size[0]))
#    ary = ary.reshape(im.size)
    return m2list(ary)


def center(l):
    xx = map(lambda (p): p[0],l)
    yy = map(lambda (p): p[1],l)
    xc = min(xx) + (max(xx)-min(xx))/2
    yc = min(yy) + (max(yy)-min(yy))/2
    return [xc,yc]


def rotate_point(point,angle):
    phi = float(angle) / (180/math.pi)
    n = matrix([[point[0], point[1], 1]])
    m = matrix([[cos(phi), sin(phi), 0],[-sin(phi),cos(phi),0], [0, 0, 1]])
    r = n*m
    rl = r.tolist()
    return (rl[0][0], rl[0][1])


def rotate(l, angle):
    (xc,yc) = center(l)
    l2 = map(lambda (x): (x[0]-xc,x[1]-yc), l)
    l2r = map(lambda (x): rotate_point(x,angle), l2)
    lr = map(lambda (x): (x[0]+xc,x[1]+yc), l2r)
    return lr


def move(l,(xdiff,ydiff):
    lm = map(lambda (p): (p[0]+xdiff,p[1]+ydiff), l)
    return lm


def find_nearest(point,l):
    nearest = None
    min_dist = 100000000000
    for p in l:
        dist = sqrt(pow(p[0]-point[0],2) + pow(p[1]-point[1],2))
        if dist < min_dist:
            min_dist = dist
            nearest = p
#    return nearest
    return min_dist


def calc_e(ldst,lsrc):
    dists = map(lambda (x): find_nearest(x,lsrc),ldst)
    tmp = map(lambda (dist): 1/(1+pow(dist,2)),dists)
    e = sum(tmp)/len(ldst)
    return e


def move_to_center(l):
    (xc,yc) = center(l)
    return move(l,(xc,yc))


#def check(c1,c2)
