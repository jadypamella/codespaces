A = [-1, -3]

def solution(A):
    A = list(filter(lambda x: x > 0, A))
    if len(A) == 0:
        return 1
    A.sort()
    next_expected = 1
    for i in range(len(A)):
        if A[i] >= next_expected:
            if A[i] == next_expected:
                next_expected += 1
            else:
                return next_expected
    #return A[-1] + 1

print(solution(A))

