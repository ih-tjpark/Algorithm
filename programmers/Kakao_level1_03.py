#https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = 0
    
    num_dic = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    
    s_len = 3
    count = len(s)
    result = ''
    
    #print(s[s_len:])
    while(1):
        #print(s)
        if count == 0:
            break
        
        if s[0].isdigit():
            result += s[0]
            count -= 1
            s = s[1:]
        
        elif s[:s_len] in num_dic:
            result += num_dic[s[:s_len]]
            s = s[s_len:]
            count -= s_len
            s_len = 3
            
        else:
            s_len += 1
            
        #print(result)
        
    answer = int(result)
        
        
        
    return answer

"""
#다른사람 풀이
def solution(s):
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)
"""