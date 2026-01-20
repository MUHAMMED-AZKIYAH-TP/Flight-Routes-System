from collections import deque
import heapq


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

        
        route = getattr(current, "airportroute", None)
        if route:
            for child in [route.left, route.right]:
                if child and child.id not in visited:
                    dfs(child, total + route.duration_min)

        
        parent_routes = current.left_node.all() | current.right_node.all()
        for parent_route in parent_routes:
            parent = parent_route.airport
            if parent.id not in visited:
                dfs(parent, total + parent_route.duration_min)

        visited.remove(current.id)

    dfs(root_airport, 0)
    return max_node, max_duration


def find_shortest_path_from_airport(root_airport):
    visited = set()
    distances = {root_airport.id: 0}
    heap = [(0, root_airport.id, root_airport)]

    min_node = root_airport
    min_duration = 0

    while heap:
        current_distance, _, current = heapq.heappop(heap)

        if current.id in visited:
            continue

        visited.add(current.id)

        # Update shortest node (excluding root itself)
        if current_distance > 0 and (
            min_node == root_airport or current_distance < min_duration
        ):
            min_node = current
            min_duration = current_distance

        # ---------- FORWARD ----------
        route = getattr(current, "airportroute", None)
        if route:
            for child in [route.left, route.right]:
                if child and child.id not in visited:
                    new_distance = current_distance + route.duration_min
                    if new_distance < distances.get(child.id, float("inf")):
                        distances[child.id] = new_distance
                        heapq.heappush(
                            heap, (new_distance, child.id, child)
                        )

        # ---------- BACKWARD ----------
        parent_routes = current.left_node.all() | current.right_node.all()
        for parent_route in parent_routes:
            parent = parent_route.airport
            if parent.id not in visited:
                new_distance = current_distance + parent_route.duration_min
                if new_distance < distances.get(parent.id, float("inf")):
                    distances[parent.id] = new_distance
                    heapq.heappush(
                        heap, (new_distance, parent.id, parent)
                    )

    return min_node, min_duration


