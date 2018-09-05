import time
import nearest_neighbor as nn

"""
********************************************************************************
* Description: two_opt function
********************************************************************************
"""
def two_opt(existing_route, start_time, mode):
    improve_attempt = 0
    route_length = len(existing_route)
    tries = 20
    while improve_attempt < tries:
        existing_distance = nn.get_total_distance(existing_route)
        for i in range(0, route_length - 1):
            if mode and time.time() - start_time > 157:
                break
            for k in range(1, route_length):
                # copy list to preserve existing in case no improvement
                new_route = existing_route[:]
                two_opt_swap(new_route, i, k)
                new_distance = nn.get_total_distance(new_route)
                # check if we've had an improvement, reset if so
                if new_distance < existing_distance:
                    existing_distance = new_distance
                    existing_route = new_route
                    improve_attempt = 0
        improve_attempt += 1

    return existing_route, existing_distance
"""
********************************************************************************
* Description: two_opt_swap function
* Function swaps two cities in a tour. In order to preserve the tour, all
* nodes in between the two being swapped are reversed.
* Note: This function mutates the 'route' parameter
********************************************************************************
"""
def two_opt_swap(route, i, k):
    if (i == 0):
        route[:k+1] = route[k::-1]
    else:
        route[i:k+1] = route[k:i-1:-1]
