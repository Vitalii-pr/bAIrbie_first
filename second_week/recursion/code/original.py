import re
import os
from pathlib import Path
import psutil
import time

def build_graph_from_note(path_to_file: str, graph=None):
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

    sorted_graph = {key: build_graph_from_note(value, {}) if isinstance(value, dict) else value for key, value in sorted(graph.items())}
    return sorted_graph

def convert_to_dot(graph: dict) -> None:
    with open("graph.dot", 'w', encoding="utf-8") as f:
        f.write("digraph {\n")
        for point in sorted(graph.keys()):
            for elem in sorted(graph[point]):
                f.write(f"{point} -> {elem}\n")
        f.write("}")

process = psutil.Process(os.getpid())
sum_time = 0
sum_memory = 0

graph = build_graph_from_note("D:/UCU/OP/Miniproject2/bAIrbie_first/second_week/recursion/test_files/node.md")

# memory_before = process.memory_info().rss / (1024 )
# start_time = time.time()

# convert_to_dot(graph)

# end_time = time.time()
# memory_after = process.memory_info().rss / (1024)
# elapsed_time = (end_time - start_time) * 1000

# print("Execution time:", elapsed_time)
# print("Difference:", memory_after-memory_before, "KB")

for i in range(1000):
    memory_before = process.memory_info().rss / (1024 )
    start_time = time.time()

    convert_to_dot(graph)

    end_time = time.time()
    memory_after = process.memory_info().rss / (1024)
    elapsed_time = (end_time - start_time) * 1000
    sum_time += elapsed_time
    sum_memory += memory_after-memory_before


# for i in range(1000):
#     memory_before = process.memory_info().rss / (1024 )
#     start_time = time.time()

#     build_graph_from_note("D:/UCU/OP/Miniproject2/bAIrbie_second/test_files/node.md")

#     end_time = time.time()
#     memory_after = process.memory_info().rss / (1024)
#     elapsed_time = (end_time - start_time) * 1000
#     sum_time += elapsed_time
#     sum_memory += memory_after-memory_before

print("Execution time:", sum_time)
print("Difference:", sum_memory, "KB")