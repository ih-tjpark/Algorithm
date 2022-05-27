#https://programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = []
    # 유저 아이디 id_list
    # 신고된 유저 아이디 report
    # 신고 정지 상한선 k
    
    #id_dict = dict.fromkeys(id_list,[]) # 리스트 주소가 동일해져서 오류발생
    
    id_dict = dict([(key,[]) for key in id_list])
    result_dict = dict.fromkeys(id_list,0)
    
    for re in report:
        re = re.split()
        if re[0] not in id_dict[re[1]]:
            id_dict[re[1]].append(re[0])
            

    for dic in id_dict:
        if len(id_dict[dic]) >= k:
            for i in id_dict[dic]:
                 result_dict[i] += 1
        
    answer = list(result_dict.values())

    return answer