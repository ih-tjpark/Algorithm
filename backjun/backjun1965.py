import sys

n = int(sys.stdin.readline())

size_list = list(map(int,sys.stdin.readline().strip().split()))
dp_list=[0 for _ in range(n)]
print(dp_list)

for i,size in enumerate(size_list):
    # 자기보다 작은 요소의 Dp값중 제일 큰 값 찾고 거기에 +1 해줌
    if i==0:
        dp_list.append(1)
    else:
        li=[]
        for j in range(i):
            
            if size > size_list[j]:
                li.append(dp_list[j])

        max(li)+1 

        new_list = list(dict.fromkeys(size_list[:i+1]))
        
        print(new_list)
        for j in new_list:
            if j <= size:
                num+=1
        dp_list.append(num)
    print(dp_list)
    

    # new_list = list(dict.fromkeys(size_list2))
    # num =0
    # #print(new_list)
    # for i in new_list:
    #     if box > i:
    #         #print(box,i)
    #         num+=1
    # num_list.append(num)
    
    # #print(num_list)
    # # if  max(num_list) < i:
    # #     break

print(max(dp_list))
 