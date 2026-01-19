from collections import deque


def find_nth_node(root_airport, direction, n):
    queue = deque([(root_airport, 1)])

    while queue:
        airport, level = queue.popleft()
        if level == n:
            return airport

        route = getattr(airport, "airportroute", None)
        if not route:
            continue

        child = getattr(route, direction)
        if child:
            queue.append((child, level + 1))

    return None
