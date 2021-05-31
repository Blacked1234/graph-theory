import json
loaded_graph = {}


def load_file(filename):
    global loaded_graph
    with open(filename) as json_file:
        loaded_graph = json.load(json_file)


infinity = 999999


def dijkstra(graph, start, end):
    dist_path = {}
    unseenNodes = graph
    dist_path[start] = 0

    for edge in graph:
        if not edge[0] in dist_path:
            dist_path[edge[0]] = infinity

    while unseenNodes:

        min_dist = None

        for node in unseenNodes:
            if min_dist is None:
                min_dist = node
            elif dist_path[min_dist] > dist_path[node]:
                min_dist = node

        path_opt = graph[min_dist].items()

        for child_node, weight in path_opt:
            if weight + dist_path[min_dist] < dist_path[child_node]:
                dist_path[child_node] = weight + dist_path[min_dist]

        unseenNodes.pop(min_dist)

    if dist_path[end] != infinity:
        print(str(dist_path[end]))
    else:
        print("No connection!")


load_file('example.json')
dijkstra(loaded_graph, 'A', 'C')

load_file('example2.json')
dijkstra(loaded_graph, 'A', 'L')

