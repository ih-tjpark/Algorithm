def solution(numbers, target):
    global answer
    answer = 0
    
    numbers_len = len(numbers)
    
    # dfs를 활용한 완전탐색
    def dfs(prev_result, idx):
        result = 0
        global answer
        
        if idx < numbers_len:
            result = prev_result + numbers[idx]
            dfs(result, idx+1)
            
            result = prev_result - numbers[idx]
            dfs(result, idx+1)
            
        else:
            if prev_result == target:
                answer += 1
            return

    dfs(0, 0)
        
    return answer