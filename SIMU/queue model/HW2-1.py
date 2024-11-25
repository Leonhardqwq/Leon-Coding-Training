import numpy as np
import math

a = np.array([0,0,1.73,1.35,0.71,0.62,14.28,0.70,15.52,3.15,1.76])
s = np.array([0,2.90,1.76,3.39,4.52,4.46,4.36,2.07,3.36,2.37,5.38])
startW = np.zeros_like(a)
endW = np.zeros_like(a)
w = np.zeros_like(a)

t = 0

###[l,r)
l = 1
r = 1

B = False
Q = 0

while True:
    if l==11:
        break

    elif l==r or (r<=10 and a[r] <= s[l]):
        if l == r:
            t=t+a[r]
        elif r<=10 and a[r] <= s[l]:
            t=t+a[r]
            s[l]=s[l]-a[r]
        print("At %.2f" % t)
        print(r, "arrive")
        r=r+1
        if r-l>1 and r<=11:
            w[r-1] = t

    else:
        t=t+s[l]
        if r<=10:
            a[r]=a[r]-s[l]
        print("At %.2f" % t)
        print( l, "depart")
        l=l+1
        if l<=10 and w[l]>0:
            w[l] = t - w[l]

    if r-l<=1:
        Q=0
    else:
        Q=r-l-1

    if not B and l<r:
        B = True
    elif B and l==r:
        B = False

    print("Q = %d B =" % Q ,B,'\n')

print("mean waiting time:%4f"%w[1:11].mean())



