def solution(n):
  # table[i][j] represents the number of ways to build a staircase with `i` bricks and max step height of `j`
  # at the end of the calculations, table[n][n] is the solution
  table = [[0 for _ in range(n+1)] for _ in range(n+1)]
  i = 1
  for i in range(1, n+1):
    for j in range(1, n+1):
      first_step = 1
      while first_step < i and first_step <= j:
        remaining_bricks = i - first_step
        other_steps_max_height = first_step - 1
        table[i][j] += table[remaining_bricks][other_steps_max_height] + (0 if remaining_bricks >= first_step else 1)
        first_step += 1
  return table[n][n]

print(solution(200))
