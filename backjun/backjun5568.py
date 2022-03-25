import sys
from itertools import combinations,permutations

n= int(sys.stdin.readline())
k = int(sys.stdin.readline())

num_list = [sys.stdin.readline().strip() for _ in range(n)]
#print(num_list)
set_list=set(permutations(num_list,k))
result =set()
for per in set_list:
    result.add(''.join(per))

print(len(result))


