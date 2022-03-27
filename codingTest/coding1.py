def solution(code, message):

    dic_s={}
    dic_n={}
    for i,c in enumerate(code):
        i+=1
        if i <10:
            dic_s[c] = '0'+str(i)
            dic_n['0'+str(i)] = c
        else:
            dic_s[c] = str(i)
            dic_n[str(i)] = c
    
    print(dic_s)
    print(dic_n)
    result=''
    mli=[]
    if message.isnumeric():

        mli = [message[s:s+2] for s in range(0,len(message),2)]
        mli = [dic_n[n] for n in mli]
    else:
        mli = [dic_s[s] for s in message]


    result = ''.join(mli)
    return result

code = "abcdefghijklmnopqrstuvwxyz"

message="20051920"
print(solution(code, message))