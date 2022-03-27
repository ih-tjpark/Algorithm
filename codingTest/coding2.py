instruction=["RIGHT 59","RIGHT","RIGHT","HALT","LEFT","LEFT","LEFT"]


dic = {'RIGHT':90,'LEFT':-90,'TURN':180}

result=0
for i in instruction:

    a = i.split()
    #print(a)
    if a[0] == 'HALT':
        break
    if len(a)==1:
        result += dic[a[0]]

    elif a[0] == 'TURN':
        result += dic[a[0]]

    else:
        result += dic[a[0]]/90 * int(a[1])
    
    
    if result>=360:
        result= result % 360
    elif result<0:
        result +=360
    #print(result)
print(result)