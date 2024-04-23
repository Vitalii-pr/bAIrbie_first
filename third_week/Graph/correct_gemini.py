# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None.

def get_graph_from_file(file_name):
    """ 
    (str) -> (list)
    
    Read graph from file and return a list of edges.
    
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    edges = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            edge = [int(node) for node in line.strip().split(',')]
            edges.append(edge)
    return edges

def to_edge_dict(edge_list):
    """ 
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.
    
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    graph_dict = {}
    for edge in edge_list:
        if edge[0] in graph_dict:
            graph_dict.update({edge[0]: sorted(graph_dict[edge[0]]+[edge[1]])})
        else:
            graph_dict[edge[0]] = [edge[1]]
        edge = edge[::-1]
        if edge[0] in graph_dict:
            graph_dict.update({edge[0]: sorted(graph_dict[edge[0]]+[edge[1]])})
        else:
            graph_dict[edge[0]] = [edge[1]]
    return graph_dict

def is_edge_in_graph(graph, edge):
    """ 
    (dict, tuple) -> bool
    
    Return True if graph contains a given edge and False otherwise.
    
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    node1, node2 = edge
    return node1 in graph and node2 in graph[node1]

def add_edge(graph, edge):
    """ 
    (dict, tuple) -> dict
    
    Add a new edge to the graph and return new graph. 
    
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    node1, node2 = edge
    # Додає вершину, якщо вона ще не існує в словнику
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    # Додає зв'язки тільки якщо ребро ще не присутнє
    if not is_edge_in_graph(graph, edge):
        graph[node1].append(node2)
        graph[node2].append(node1)

    return graph

def del_edge(graph, edge):
    """ 
    (dict, tuple) -> (dict)
    
    Delete an edge from the graph and return a new graph.
    
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    node1, node2 = edge

    # Перевірте, чи існує ребро у графі
    if is_edge_in_graph(graph, edge):
        graph[node1].remove(node2)
        graph[node2].remove(node1)

    return graph

def add_node(graph, node):
    """ 
    (dict, int) -> (dict)
    
    Add a new node to the graph and return a new graph.
    
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node not in graph:
        graph[node] = []
    return graph

def del_node(graph, node):
    """ 
    (dict, int) -> (dict)
    
    Delete a node and all incident edges from the graph.
    
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    for neighbor in graph.get(node, []):
        if neighbor in graph:
            graph[neighbor].remove(node)
    graph.pop(node, None)
    return graph

def convert_to_dot(filename:str)->None:
    """
    Get graph from a file and save the directed graph to a file in a DOT format with the same name.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        pairs = []
        for line in file:
            a, b = map(int, line.strip().split(','))
            pairs.append([a, b])
            pairs.append([b, a])
        pairs.sort()
    with open(filename.replace('.txt', '.dot'), 'w', encoding='utf-8') as file:
        file.write('digraph {\n')
        file.write('\n'.join([f'{x[0]} -> {x[1]}' for x in pairs]))
        file.write('\n}')

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
