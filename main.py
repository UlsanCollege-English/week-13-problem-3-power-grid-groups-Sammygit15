def count_power_groups(stations, lines):
    # Build adjacency list
    graph = {s: set() for s in stations}

    for a, b in lines:
        graph[a].add(b)
        graph[b].add(a)

    visited = set()
    groups = 0

    # BFS or DFS to explore each component
    from collections import deque

    for station in stations:
        if station not in visited:
            groups += 1

            # BFS exploration
            queue = deque([station])
            visited.add(station)

            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

    return groups


if __name__ == "__main__":
    # Optional manual test
    stations = ["A", "B", "C", "D"]
    lines = [("A", "B"), ("B", "C")]
    print(count_power_groups(stations, lines))  # expected 2
