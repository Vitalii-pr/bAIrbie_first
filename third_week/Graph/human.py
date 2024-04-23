'''graph'''
def get_graph_from_file(file_name: str) -> list:
    """ 
    (str) -> (list)
    The function must read data from a file into 
    file_name and return a list of graph edges.
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r', encoding = 'UTF-8') as file:
        result = []
        list_graph= file.readlines()
        for element in list_graph:
            element = element.strip().split(',')
            result.append([int(element[0]), int(element[1])])
    return result

def to_edge_dict(edge_list: list) -> dict:
    """ 
    (list) -> (dict)
    The function must convert a list of graph edges into a dictionary
    of vertices.
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    result = {}
    for element in edge_list:
        if element[0] in result:
            result.update({element[0]: sorted(result[element[0]]+[element[1]])})
        else:
            result[element[0]] = [element[1]]
        element = element[::-1]
        if element[0] in result:
            result.update({element[0]: sorted(result[element[0]]+[element[1]])})
        else:
            result[element[0]] = [element[1]]
    return result

def is_edge_in_graph(graph: dict, edge: tuple) -> bool:
    """ 
    (dict, tuple) -> bool
    Return True if graph contains a given edge and False otherwise.
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    if edge[0] in graph:
        if edge[1] in graph[edge[0]]:
            return True
    return False

def add_edge(graph: dict, edge: tuple) -> dict:
    """ 
    (dict, tuple) -> dict
    The function must add a new edge to the graph. The graph is passed 
    to the function as a dictionary. If the edge is already present in 
    the graph, the function must return the graph unchanged. An edge can 
    be added to a graph even if one of its vertices is missing.
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    if edge[0] not in graph[edge[1]] or edge[1] not in graph[edge[0]]:
        if edge[0] in graph :
            graph[edge[0]].append(edge[1])
        else:
            graph[edge[0]] = [edge[1]]
        if edge[1] in graph:
            graph[edge[1]].append(edge[0])
        else:
            graph[edge[1]] = [edge[0]]
    return graph

def del_edge(graph: dict, edge: tuple) -> dict:
    """ 
    (dict, tuple) -> (dict)
    Delete an edge from the graph and return a new graph.
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if edge[0] in graph:
        try:
            graph[edge[0]].remove(edge[1])
        except ValueError:
            pass
    if edge[1] in graph:
        try:
            graph[edge[1]].remove(edge[0])
        except ValueError:
            pass
    return graph

def add_node(graph: dict, node:int) -> dict:
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
    pass

def convert_to_dot(filename:str)-> None:
    """
    Get graph from a file and save the directed graph to a file in a DOT format with the same name.
    """
    pass

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
