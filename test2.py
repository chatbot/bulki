from misc import *
from scipy.optimize import fmin, fmin_powell, fmin_bfgs, anneal, brute,fmin_cobyla
from PIL import Image, ImageDraw

src = loadcontour('data/source2.png')

(xc,yc) = center(src)
src = map(lambda (p): (p[0]-xc,p[1]-yc), src)

# files must be the same size
files = ['data/d4z.gif']#,'data/d2.png','data/d3.png','data/d4.png')


im = Image.open(files[0])
(w,h) = im.size
ans = zeros(w*h)
ans = ans.reshape((h,w))


ii=0
j=0
def f(xy,*args):
    global ans,ii
    global j
    (x,y,z) = xy
    curr = rotate(src,z)
    curr = move(curr,(x,y))
    e = round(calc_e(dest,curr)*100)/100
    print x,y,z,e
    #e = calc_e(dest,curr)
    #ans[x][y]=e
    #print x,y,e
    im = Image.open('data/white.png')
    draw = ImageDraw.Draw(im)

    draw.point(dest,fill=127)
    draw.point(curr,fill=0)
    im.save('sol'+str(j)+'/'+str(ii)+'.png')
    ii+=1
    return e



for (i,file) in enumerate(files):
    dest = loadcontour(file)
    (xc2,yc2) = center(dest)
    #r = fmin(f,[xc2-15,yc2-15],xtol=0.1)

    diffs = [(0,0)]
    for diff in diffs:

        #while len(dest) > len(curr)/4

        solution = fmin(f,[xc2+diff[0],yc2+diff[1],0],xtol=0.1)
        print solution
        j+=1
        ii=0
 #   i=0
 #   for step in solution[0]:
 #       print 'fuck!', step
 #       x,y,z = step
        
 #       curr = rotate(src,z)
 #       curr = move(curr,(x,y))

        #print x,y,z
#        i+=1





#    for y in range(yc2-30,yc2+30):
#        for x in range(xc2-20,xc2+20):
#            curr = move(src,(x,y))
#            e = calc_e(dest,curr)
#            ans[x][y] += e
#            print i,x,y,e




s = "\n".join(map(lambda (x): " ".join(map(str,x)), ans))
f=open("path.dat","w")
f.write(s)
f.close()



        
