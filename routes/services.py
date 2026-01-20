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











def find_longest_path(root_airport):
    visited = set()
    max_duration = 0
    max_node = root_airport

    def dfs(current, total):
        nonlocal max_duration, max_node

        visited.add(current.id)

        if total > max_duration:
            max_duration = total
            max_node = current

        # FORWARD: current -> children
        route = getattr(current, "airportroute", None)
        if route:
            for child in [route.left, route.right]:
                if child and child.id not in visited:
                    dfs(child, total + route.duration_min)

        # BACKWARD: parent -> current
        parent_routes = current.left_node.all() | current.right_node.all()
        for parent_route in parent_routes:
            parent = parent_route.airport
            if parent.id not in visited:
                dfs(parent, total + parent_route.duration_min)

        visited.remove(current.id)

    dfs(root_airport, 0)
    return max_node, max_duration