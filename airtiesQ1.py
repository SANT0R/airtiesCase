


Days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat","Sun"]


def solution(S,K):

    toDay = Days.index(S)
    nextDay = K%7

    return Days[(toDay+nextDay)%7]






print(solution("Wed",243))