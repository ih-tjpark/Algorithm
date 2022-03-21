import sys
N, K = map(int,sys.stdin.readline().split())
data=[(sys.stdin.readline().strip().split()) for i in range(K)]

data =sum(data,[])

board= ['?' for i in range(N)]

num= data
#print(num)
n=0
where=0
final = ''
for i in range(K):
    
    #print(board)
    a = int(num[n])
    
    
    where += int(num[n]) % N
    

    if where+1 > N:
        where = where - N
        #if where<=-1:
        #    where=0
        #print(where)

    #print(num[n],'',num[n+1])
    final = num[n+1]
    if board[where] =='?' and num[n+1] not in board:
        board[where] = num[n+1]
        n+=2
    elif num[n+1] == board[where]:
        n+=2
        continue
    else:
        board=['!']
        break

if board[0]=='!':
    print('!')
else:
    #print(board.index(final))
    out_index = board.index(final)
    for j in range(N):
        
        if out_index < 0:
            out_index = N-1
        
        print(board[out_index],end='')
        out_index-=1