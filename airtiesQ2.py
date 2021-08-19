

def solution(N):

    resault = []

    for i in range(N):
        if i % 2 == 0:
            resault.append("+")
        else:
            
            resault.append("-")
    
    return resault



print(solution(4))