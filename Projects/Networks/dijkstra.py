import heapq

def dijkstra(graph, src):
    # define a dictionary that stores the shortest distance from src
    distance_graph = {node: float("inf") for node in graph}
    distance_graph[src] = 0

    # define a dictionary that stores the shortest path
    path = {node: [] for node in graph}
    path[src] = [src]

    # priority queue (min-heap) for selecting the next node with smallest distance
    pq = [(0, src)] # (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # skip if we found a path with a smaller cost already
        if current_distance > distance_graph[current_node]:
            continue

        for neighbour, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distance_graph[neighbour]:
                distance_graph[neighbour] = distance
                path[neighbour] = path[current_node] + [neighbour]
                heapq.heappush(pq, (distance, neighbour))

    return distance_graph, path

if __name__ == "__main__":
    graph = {
    "u": {"a": 2, "c": 1, "d": 3},
    "a": {"u": 2, "c": 2, "b": 4},
    "b": {"a": 4, "c": 2, "e": 2},
    "c": {"u": 1, "a": 2, "b": 2, "d": 1, "e": 5},
    "d": {"u": 3, "c": 1, "g": 3},
    "e": {"c": 5, "h": 1},
    "f": {"c": 8, "g": 3, "h": 1},
    "g": {"d": 3, "f": 3},
    "h": {"e": 1, "f": 1}
    }

    distance, path = dijkstra(graph, "u")
    print("Shortest Distances: ", distance)
    print("Shortest Paths: ", path)