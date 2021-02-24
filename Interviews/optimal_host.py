import math


def optimal_host(friends):
    assert len(friends) > 0
    best_host = None
    best_cost = 1e100

    for potential_host in friends:
        l = potential_host['location']

        cost = sum(math.sqrt((l[0] - person['location'][0])**2 +\
                             (l[1] - person['location'][1])**2 +\
                             (l[2] - person['location'][2])**2) for person in friends)

        if cost < best_cost:
            best_cost = cost
            best_host = potential_host

    return best_host, best_cost


friends = [
    {'name': 'Bob', 'location': (5, 2, 10)},
    {'name': 'David', 'location': (2, 3, 5)},
    {'name': 'Mary', 'location': (19, 3, 4)},
    {'name': 'Skyler', 'location': (3, 5, 1)},
]

print(optimal_host(friends))