import sys
import time
from bisect import bisect_left
import numpy as np
start = time.time()
T = int(sys.stdin.readline())


for _ in range(T):
    N = int(sys.stdin.readline())
    n=1
    sum_=0
    if N==1:
        print(1)
    else:
        print(bisect_left(in_array, x=N)) 

    # while(sum_<N):
    #     n+=1
    #     sum_+=n
    # if N==1:
    #     print(1)
    # else:
    #     print (n-1)

#end = time.time()

#print(end-start)

# i = 1000000
# n=0
# sum_=0
# while sum_<i:
#     n+=1

#     sum_+=n

# print(n)

    