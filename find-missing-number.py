def solution(A):
    print(A)
    smallest = sorted(A)[0]
    highest = sorted(A)[len(A) - 1]
    if (highest + 1 == 0):
        missing_number = 1
    else:
        missing_number = highest + 1
    for i in range(smallest, highest, 1):
        if ((i not in A) & (i > 0)):
            missing_number = i
            break
    return missing_number

# print(solution(A=[-1, -3]))
print(solution(A=[1, 5, 3, 1, 5, 6]))
# print(solution(A=[1, 2, 3]))