def solution(nums):
    
    s = set(nums)
    n = len(nums)
    answer = 0
    
    if int(n/2) > len(s):
        answer = len(s)
    else:
        answer = int(n/2)
    
    return answer