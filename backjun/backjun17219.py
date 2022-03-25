import sys

N, M = map(int,(sys.stdin.readline().split()))

dict ={}
for _ in range(N):

    address, pwd = sys.stdin.readline().split()
    dict[address] = pwd
#print(dict)
for _ in range(M):
    print(dict[sys.stdin.readline().strip()])
#print(N,M)