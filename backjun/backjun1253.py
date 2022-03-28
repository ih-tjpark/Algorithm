import sys
from bisect import *

N = int(sys.stdin.readline().strip())

A = list(map(int,sys.stdin.readline().split()))

#본인 제외하고 더하여 본인 숫자가 되는 수 찾기
A.sort()
B_list = A
n = 0
num=0
result = 0

while(1):
    
    back = A.pop()
    print(A)
    if len(A)<=1:
        break
    for i in A[::-1]:
        if back == i+A[bisect_left(A, back-i)]:
            #print(A[bisect_left(A, back-i)])
            result+=1
            print(result)
            break
            

print(result)
    



#li=list(combinations(A, 2))


# print(li)
# for i in li:
#     if 
#     numSet.add(i[0]+i[1])
# #print(numSet)
# #print(A)
# result=0
# for i in A:
    
#     if i in numSet:
#         result+=1
# print(result)
#for i in A:

#    if  
