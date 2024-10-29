import heapq

def dijkstra(graph, start):
  distances = {vertex: float('inf') for vertex in graph}
  distances[start] = 0
  visited = set()
  priority_queue = [(0, start)]  # Використовуємо купу для зберігання вершин

  while priority_queue:
    current_distance, current_vertex = heapq.heappop(priority_queue)

    if current_vertex in visited:
      continue

    visited.add(current_vertex)

    for neighbor, weight in graph[current_vertex].items():
      distance = current_distance + weight
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        heapq.heappush(priority_queue, (distance, neighbor))

  return distances


# Приклад використання:
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 1, 'E': 3},
    'D': {'B': 5, 'C': 1, 'E': 1},
    'E': {'C': 3, 'D': 1},
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in shortest_distances.items():
  print(f"{vertex}: {distance}")