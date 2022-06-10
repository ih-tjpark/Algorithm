def solution(phone_book):
    answer = True
    '''
    #효율성 error
    for i in range(len(phone_book)):
        num_len = len(phone_book[i])
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][:num_len]:
                return False
     '''       
    phone_book.sort(key= lambda x: len(x))
    #print(phone_book)
    
    num_len = len(phone_book[0])
    check_dic = dict.fromkeys([j[:num_len] for j in phone_book if len(j) > num_len])
    for i in phone_book:
        if num_len != len(i):
            num_len = len(i)
            check_dic = dict.fromkeys([j[:num_len] for j in phone_book if len(j) > num_len])
            if i in check_dic:
                return False
        else:
            if i in check_dic:
                return False
        
    #phone_dic = [i[:3] for i in phone_book]
    
    return answer