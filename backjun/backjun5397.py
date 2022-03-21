import sys
from collections import deque

num =int(sys.stdin.readline())

data=[(sys.stdin.readline().strip().split()) for i in range(num)]


for i in range(num):
    main_stack = deque()
    sub_stack = deque()

    for string in data[i][0]:

        if string == '<':
            if not main_stack:
                continue
            else:
                sub_stack.append(main_stack.pop())
        
        elif string == '>':
            if not sub_stack:
                continue
            else:
                main_stack.append(sub_stack.pop())

        elif string == '-':
            if not main_stack:
                continue
            else:
                main_stack.pop()
        
        else:
            main_stack.append(string)
        
    if sub_stack:
        for i in range(len(sub_stack)):
            main_stack.append(sub_stack.pop())
    
    
    print(''.join(main_stack))
        




