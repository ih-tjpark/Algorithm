def solution(n, lost, reserve):
    
    answer = 0

    clothe_dic = {i+1:1 for i in range(n)}
    
    for los in lost:
        clothe_dic[los] -= 1
    
    for res in reserve:
        clothe_dic[res] += 1
    
    for key in clothe_dic:
        if clothe_dic[key] == 0:
            if key == 1: 
                if clothe_dic[key+1] == 2:
                    clothe_dic[key], clothe_dic[key+1] = 1, 1

            elif key == n:
                if clothe_dic[key-1] == 2:
                    clothe_dic[key], clothe_dic[key-1] = 1, 1

            else: 
                if clothe_dic[key-1] == 2:
                    clothe_dic[key], clothe_dic[key-1] = 1, 1
                
                elif clothe_dic[key+1] == 2:
                    clothe_dic[key], clothe_dic[key+1] = 1, 1
                    
    answer = n 
    for los in lost:
        if clothe_dic[los] == 0:
            answer -= 1    


    return answer