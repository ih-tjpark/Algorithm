#https://programmers.co.kr/learn/courses/30/lessons/72410

import re

def solution(new_id):
    
    answer = ''
    
    new_id = new_id.lower()
    
    new_id = re.sub(r'[^0-9a-z-_.]','',new_id)
    
    new_id = re.sub(r'\.{2,}','.',new_id)

    new_id = re.sub(r'\A\.|\.\Z','',new_id)
    
    if len(new_id) == 0:
        new_id = 'a'
    
    elif len(new_id) >= 16:
        new_id = new_id[:15]
        new_id = re.sub(r'\.\Z','',new_id)
    
    if len(new_id) <= 2:
        new_id += new_id[-1]*(3-len(new_id))
    
    #print(new_id)
    
    answer = new_id
    
    return answer