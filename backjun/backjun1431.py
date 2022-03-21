import sys


N = int(sys.stdin.readline())

lines = [(sys.stdin.readline().strip()) for _ in range(N)]

#print(lines)

def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            
            #길이가 길면 swap
            if len(arr[i-1])> len(arr[i]):
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
            
            #길이가 같고
            if len(arr[i-1]) == len(arr[i]):
                n1=0
                n2=0
                for x,y in zip(arr[i-1],arr[i]):
                    if x.isnumeric():
                        n1+=int(x)
                    if y.isnumeric():
                        n2+=int(y)
                if n1>n2:
                    arr[i-1], arr[i] = arr[i], arr[i-1]
                
                elif n1==n2:
                    if arr[i-1]>arr[i]:
                        arr[i - 1], arr[i] = arr[i], arr[i - 1]
                  
    return arr

for array in insertion_sort(lines):
    print(array)







