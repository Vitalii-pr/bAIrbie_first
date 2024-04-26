'''.'''
import re
import os
from pathlib import Path

def build_graph_from_note(path_to_file: str, graph=None):
    """
    ...
    >>> 1
    1
    """
    if graph is None:
        graph = {}

    original_file_name, _ = os.path.splitext(os.path.basename(path_to_file))
    dir_name = os.path.dirname(path_to_file)

    with open(path_to_file, 'r', encoding="utf-8") as file:
        matches = re.findall(r"\[\[(.*?)\]\]", file.read())
        if original_file_name not in graph:
            if matches:
                graph[original_file_name] = sorted(matches)
            for match in matches:
                next_file_path = Path(dir_name) / (match + ".md")
                if next_file_path.is_file():
                    build_graph_from_note(str(next_file_path), graph)

    sorted_graph = {key: build_graph_from_note(value, {}) if isinstance(value, dict)
else value for key, value in sorted(graph.items())}
    return sorted_graph

def convert_to_dot(graph:str):
    """
    The convert_to_dot(filename) function should read an initial file of edges,
      such as data1.txt, and save the oriented graph built from them to a file with 
      the same name but with the DOT extension. You can see an example of an oriented 
      graph here. It will allow you to quickly and efficiently visualize the graph 
      and check if other functions are working correctly.
    >>> 1
    1
    """
    graph=dict(sorted(graph.items()))
    for i in graph:
        graph[i]=sorted(graph[i])
    with open('graph.dot', 'w+', encoding='UTF-8') as data2:
        data2.write("digraph {\n")
        a = graph.keys()
        for i in a:
            for j in graph[i]:
                data2.write(f"{i} -> {j}\n")
        data2.write("}")

if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
