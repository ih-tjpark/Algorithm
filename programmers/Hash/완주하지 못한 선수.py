def solution(participant, completion):
    answer = ''

    
    #효율성 error
    # for c in completion:  
    #     participant.remove(c)
    # answer = participant[0]

    #효율성 error
    #p_dic = {name:participant.count(name) for name in participant}
    #c_dic = {name:completion.count(name) for name in completion}

    p_dic = dict.fromkeys(participant,0)
    c_dic = dict.fromkeys(completion,0)

    for i in range(len(participant)):
        p_dic[participant[i]] += 1
        if i < len(participant)-1:
            c_dic[completion[i]] += 1

    for p_name in p_dic:
        if p_name not in c_dic:
            answer = p_name
            break
        elif p_dic[p_name] != c_dic[p_name]:
            answer = p_name
            break

    return answer