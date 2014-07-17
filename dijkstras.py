import json

def dijkstras(adj_list):
    unvisited = {node: None for node in adj_list.keys()} #using None as +inf
    visited = {}
    current = 'B'
    prev={}
    cur_distance = 0
    unvisited[current] = cur_distance

    while True:
        for neighbour in adj_list[current].keys():
            if neighbour not in unvisited:
                continue
            newDistance = cur_distance + adj_list[current][neighbour]

            #print type(adj_list[current][neighbour])

            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                prev[neighbour]=current
                unvisited[neighbour] = newDistance
                #print unvisited
        visited[current] = cur_distance
        #print visited
        del unvisited[current]
        if not unvisited: break
        candidates = [n for n in unvisited.items() if n[1]]
        current, cur_distance = sorted(candidates, key = lambda x: x[1])[0]
        #print type(cur_distance)

    print(visited)
    #print prev


if __name__=="__main__":
    with open('graph.json') as graph:
        adj_list=json.load(graph)
    #print adj_list
    dijkstras(adj_list)
