import numpy as np
import math
M = 1000000
N = 1000000
N_ = 100
a = np.random.exponential(5,N+N_)
s1 = np.random.exponential(3,N+N_)
s2 = np.random.exponential(4,N+N_)

t_in1 = np.zeros_like(a)
t_in2 = np.zeros_like(a)
t_start1 = np.zeros_like(a)
t_start2 = np.zeros_like(a)
t_out1 = np.zeros_like(a)
t_out2 = np.zeros_like(a)

t = 0
tB1 = 0
tB2 = 0
l1 = 1
r1 = 1
l2 = 1
r2 = 1

while True:
    if l2==N:
        break

    B1_old = l1!=r1
    B2_old = l2!=r2
    t_old = t

    t_a = a[r1]
    t_s1 = s1[l1] if l1!=r1 else M
    t_s2 = s2[l2] if l2!=r2 else M
    ###arrive
    if t_a<= t_s1 and t_a<=t_s2:
        t = t + t_a
        if l1 != r1:
            s1[l1] = s1[l1] - t_a
        if l2 != r2:
            s2[l2] = s2[l2] - t_a

        t_in1[r1] = t
        if l1 == r1:
            t_start1[r1] = t
        r1 = r1 + 1

    ###s1 finish
    elif t_s1<=t_s2:
        t = t + t_s1
        a[r1] = a[r1] - t_s1
        if l2 != r2:
            s2[l2] = s2[l2] - t_s1

        t_in2[r2] = t
        if l2 == r2:
            t_start2[r2] = t
        r2 = r2 + 1
        t_out1[l1] = t
        l1 = l1 + 1
        if l1!=r1:
            t_start1[l1] = t

    ###s2 finish
    else:
        t = t + t_s2
        a[r1] = a[r1] - t_s2
        if l1 != r1:
            s1[l1] = s1[l1] - t_s2

        t_out2[l2] = t
        l2 = l2 + 1
        if l2!=r2:
            t_start2[l2] = t

    dlt_t = t-t_old
    if B1_old:
        tB1 = tB1 +dlt_t
    if B2_old:
        tB2 = tB2 +dlt_t



t_whole = t_out2 - t_in1
t_w1 = t_start1 - t_in1
t_w2 = t_start2 - t_in2
print("(a) Mean time spent in the system =",t_whole[0:N].mean())
print("(b) Mean time in queue1 =",t_w1[0:N].mean())
print("(b) Mean time in queue2 =",t_w2[0:N].mean())
print("(c) Proportion of idle time of server1  =",1-tB1/t)
print("(c) Proportion of idle time of server1  =",1-tB2/t)

t_out1_interval = np.zeros_like(a)
t_out2_interval = np.zeros_like(a)
for i in range(0,N-1):
    t_out1_interval[i] = t_out1[i+1] - t_out1[i]
    t_out2_interval[i] = t_out2[i+1] - t_out2[i]
print("(d) Mean time interval of the departure process of server1 =",t_out1_interval[0:N-1].mean())
print("(d) Mean time interval of the departure process of server2 =",t_out2_interval[0:N-1].mean())
