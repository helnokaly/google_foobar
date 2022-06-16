def solution(s):
    right = 0
    salutes = 0
    for c in s:
        if c == '>':
            right += 1
        elif c == '<':
            salutes += right * 2
    return salutes

# Input:
print(solution(">----<"))
# Output:
    # 2

# Input:
print(solution("<<>><"))
# Output:
    # 4