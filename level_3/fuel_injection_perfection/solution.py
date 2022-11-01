def solution(n):
  num = int(n)
  op_count = 0
  while num > 1:
    if num % 2 == 0:
      num //= 2
    elif num & 3 == 3 and num > 3:
      num += 1
    else:
      num -= 1
    op_count += 1
  return op_count


print(solution('78479437574375439758437589473857357934795'))
print(solution('3'))
print(solution('7'))