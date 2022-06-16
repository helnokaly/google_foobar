from collections import deque

def bfs(map, start_row, start_column):
  calculated_map = [[None for _ in range(len(map[0]))] for _ in range(len(map))]
  q = deque()
  q.append((start_row, start_column, 1))
  while len(q) > 0:
    row, column, current_distance = q.popleft()

    # if index out of bounds skip current invalid node
    if row < 0 or row >= len(map) or column < 0 or column >= len(map[0]): continue

    # skip if distance already calculated for current node, saves us from going in cycles
    if calculated_map[row][column] is not None: continue

    # save the distance from the start node to the current node
    calculated_map[row][column] = current_distance

    # if current node is a wall, calculate distance but do not traverse further
    if map[row][column] == 1: continue 

    # Traverse right
    q.append((row, column + 1, current_distance + 1))
    # Traverse down
    q.append((row + 1, column, current_distance + 1))
    # Traverse left
    q.append((row, column - 1, current_distance + 1))
    # Traverse up
    q.append((row - 1, column, current_distance + 1))
  
  return calculated_map


def solution(map):
  # calculate distance to all nodes from the starting node
  bfs_start = bfs(map, 0, 0)

  # calculated distance to all nodes from the ending node
  bfs_end = bfs(map, len(map) - 1, len(map[0]) - 1)

  # calculate the shortest distance by comparing each node from the two calculated matrices
  # the calculation = distance from start node to current node + from end node to current node (the meeting point)
  # the minimum of these is the shortest distance
  shortest_distance = float('inf')
  for i in range (0, len(map)):
    for j in range (0, len(map[0])):
      if bfs_start[i][j] is not None and bfs_end[i][j] is not None:
        shortest_distance = min(shortest_distance, bfs_start[i][j] + bfs_end[i][j] - 1)

  return int(shortest_distance)

# print(solution([
#   [0, 1, 1, 0], 
#   [0, 0, 0, 1], 
#   [1, 1, 0, 0], 
#   [1, 1, 1, 0]]
# ))
print(solution([
  [0, 0, 0, 0, 0, 0], 
  [1, 1, 1, 1, 1, 0], 
  [0, 0, 0, 0, 0, 0], 
  [0, 1, 1, 1, 1, 1], 
  [0, 1, 1, 1, 1, 1], 
  [0, 0, 0, 0, 0, 0]
]))
# print(solution([[0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 1, 0]]))