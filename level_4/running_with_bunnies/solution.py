# Implementation of Bellman-Ford algorithm
def bellman_ford(times, start):
  V = len(times)
  distance = [float('inf') for _ in range(0, V)]
  distance[start] = 0

  for i in range(0, V - 1):
    for edge_from in range(0, V):
      for edge_to in range(0, V):
        distance[edge_to] = min(distance[edge_to], distance[edge_from] + times[edge_from][edge_to])
  
  for i in range(0, V - 1):
    for edge_from in range(0, V):
      for edge_to in range(0, V):
        if distance[edge_from] + times[edge_from][edge_to] < distance[edge_to]:
          distance[edge_to] = -float('inf')

  return distance

# Returns the longest path from start to bulkhead while times_limit >= 0
def longest_possible_path(bellman_ford_times, times_limit, current_location = 0, visited = []):
  n_locations = len(bellman_ford_times)
  end_location = n_locations - 1
  if current_location == end_location and times_limit < 0: return []
  if current_location in visited: return []
  if current_location == end_location and times_limit >= 0: return [current_location]

  current_visited = visited + [current_location]
  best_path = []
  for next_location in range (1, n_locations):
    path = longest_possible_path(bellman_ford_times, times_limit - bellman_ford_times[current_location][next_location], next_location, current_visited)
    if len(path) > len(best_path):
      best_path = path
  
  return [] if len(best_path) == 0 else [current_location] + best_path

def solution(times, times_limit):
  V = len(times)

  # Get Bellman-Ford shortest distances starting from each location
  bellman_ford_times = [bellman_ford(times, i) for i in range (0, V)]

  # Get the longest path from start to bulkhead while times_limit >= 0
  # Then drop the first and last items in the list (start and bulkhead)
  # since we need only the bunnies locations
  saved_bunnies_locations = longest_possible_path(bellman_ford_times, times_limit)[1:-1]

  # Bunnies IDs is location - 1
  saved_bunnies = map(lambda x: x-1, saved_bunnies_locations)

  # Return sorted bunnies IDs
  return sorted(saved_bunnies)

print(solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)) # Expect: [1,2]
print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)) # Expect: [0,1]