import math

#find the distance of next node, round to nearest int
def find_distance(a, b):
    dx = a['x'] - b['x']
    dy = a['y'] - b['y']
    result = int(round(math.sqrt(dx * dx + dy * dy)))
    return result


# Greedy nearest neighbor algorithm- tour1
def nearest_neighbor(cities):
    start_city = cities[0]
    unvisited = cities[1:]
    path = [start_city]
    path_distance = 0
    while unvisited:
        min_distance = float('inf')
        for city in unvisited:
            distance = find_distance(path[-1], city)
            if min_distance > distance:
                nearest_city = city
                min_distance = distance
        path_distance += min_distance
        unvisited.remove(nearest_city)
        path.append(nearest_city)
    distance = find_distance(nearest_city, start_city)
    path_distance += distance
    return path, path_distance


#get total weight for the tour
def get_total_distance(cities):
    total_distance = 0
    last_city = None

    for i in range(0, len(cities) - 1):
        current_city = cities[i]
        next_city = cities[i + 1]

        total_distance += find_distance(current_city, next_city)
        last_city = next_city

    # Add the distance to go back to the starting city
    total_distance += find_distance(last_city, cities[0])

    return total_distance
