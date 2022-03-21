import sys
N = int(sys.stdin.readline())

numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]

numbers.sort()

result=[]
#print(numbers)

for i in range(1,N):
    result.append(int(str(numbers[0])+str(numbers[i])))
    result.append(int(str(numbers[i])+str(numbers[0])))
    if i >10:
        break

result.append(int(str(numbers[1])+str(numbers[2])))


#print(result)
result.sort()
#print(result)
print(result[2])


