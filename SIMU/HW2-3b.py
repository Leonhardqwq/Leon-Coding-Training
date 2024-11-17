import random
import numpy as np

N = 6
at = np.cumsum(np.array([2, 4, 5, 6, 3, 10]))
T_st = np.array([12, 15, 13, 16, 17, 14])
A_st = np.array([18, 15, 17, 20, 19, 13])
barber = np.empty(N, dtype='U1')
barber[:] = 'n'
is_lo = np.empty(N, dtype='U1')
is_lo[:] = 'F'
dt = np.zeros(N)
wq = np.zeros(N)
ws = np.zeros(N)
T_s = 0
A_s = 0

for i in range(N):
    if T_s <= at[i] and A_s <= at[i]:
        c = random.choice(['T', 'A'])
        wq[i] = 0
    elif min(T_s, A_s) - at[i] > 10:
        dt[i] = at[i] + 10
        wq[i] = ws[i] = 10
        is_lo[i] = 'T'
        continue
    elif T_s < A_s:
        c = 'T'
    elif A_s < T_s:
        c = 'A'
    else:
        c = random.choice(['T', 'A'])

    if c == 'T':
        wq[i] = max(T_s - at[i], 0)
        ws[i] = wq[i] + T_st[i]
        dt[i] = at[i] + ws[i]
        T_s = dt[i]
    else:
        wq[i] = max(A_s - at[i], 0)
        ws[i] = wq[i] + A_st[i]
        dt[i] = at[i] + ws[i]
        A_s = dt[i]
    barber[i] = c

for i in range(N):
    print(f"{i+1}   {at[i]}     {dt[i]}     {wq[i]}     {ws[i]}     {barber[i]}     {is_lo[i]}")
