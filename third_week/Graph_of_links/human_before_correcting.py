"""graphs"""
import re

def build_graph_from_note(note_path:str, graph = None)->dict:
    """
    building the graph
    >>> 1
    1
    """
    if graph is None:
        graph={}
    note=note_path.split('/')[-1][:-3]
    if note not in graph.keys():
        graph[note]=[]
        with open(note_path, 'r', encoding='UTF-8') as data:
            for line in data:
                graph[note]+= re.findall(r"\[\[(.*?)\]\]", line)
    for i in graph[note]:
        if i not in graph.keys():
            try:
                graph_2=build_graph_from_note("/".join(note_path.split('/')[:-0])+i+".md", graph)
                for key in graph_2.keys():
                    graph[key]=graph_2[key]
            except FileNotFoundError:
                pass
    return dict(sorted(graph.items()))
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
        for i in graph.keys():
            for j in graph[i]:
                data2.write(f"{i} -> {j}\n")
        data2.write("}")

if __name__ == "__main__":
    import doctest

    print(doctest.testmod())