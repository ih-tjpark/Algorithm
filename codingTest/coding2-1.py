
def solution(numbers):

    numbers.sort()
    result=[]
    #print(numbers)
    if len(numbers) == 1 :
        if numbers[0] == 0:
            result = [numbers[0]+1]
        else: result = [numbers[0]-1,numbers[0]+1]
        return result
    
    for i, num in enumerate(numbers):

        if i ==0:
            continue

        if num - numbers[i-1] >= 3:
            return []
        
        elif  num - numbers[i-1] == 2:
            result.append(num-1)
            if len(result) >=2:
                return []
    
    if len(result)==0:

        if numbers[0]==0:
            result = [numbers[-1]+1]
        else:
            result = [numbers[0]-1,numbers[-1]+1]

    return result


numbers = []

print(solution(numbers))