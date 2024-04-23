import unittest
import tempfile

from unittest import TestCase
from graph_gemini import get_graph_from_file, to_edge_dict, \
    is_edge_in_graph, add_edge, del_edge, add_node, del_node, convert_to_dot

class GraphTest(TestCase):
    '''testing'''
    def test_get_graph_from_file(self):
        # Test with a valid file
        result = get_graph_from_file("data1.txt")
        self.assertEqual(result, [[1, 2], [3, 4], [1, 5]])

        # Test with a non-existent file (consider mocking the file system)
        with self.assertRaises(FileNotFoundError):
            get_graph_from_file("missing_file.txt")

    def test_empty_list(self):
        result = to_edge_dict([])
        self.assertEqual(result, {})

    def test_single_edge(self):
        result = to_edge_dict([[1, 2]])
        self.assertEqual(result, {1: [2], 2: [1]})

    def test_multiple_edges(self):
        result = to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
        self.assertEqual(result, {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]})

    def test_duplicate_edges(self):
        result = to_edge_dict([[1, 2], [1, 3]])
        self.assertEqual(result, {1: [2, 3], 2: [1], 3: [1]})

    def test_is_edge_in_graph(self):
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        self.assertTrue(is_edge_in_graph(graph, (1, 2)))
        self.assertFalse(is_edge_in_graph(graph, (2, 3)))

    def test_add_edge(self):
        graph = {1: [2], 2: [1]}
        new_graph = add_edge(graph, (3, 4))
        self.assertEqual(new_graph, {1: [2], 2: [1], 3: [4], 4: [3]})

    def test_del_edge(self):
        graph = {1: [2], 2: [1]}
        new_graph = del_edge(graph, (1, 2))
        self.assertEqual(new_graph, {1: [], 2: []})

    def test_add_node(self):
        graph = {}
        new_graph = add_node(graph, 5)
        self.assertEqual(new_graph, {5: []})

    def test_del_node(self):
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        new_graph = del_node(graph, 5)
        self.assertEqual(new_graph, {1: [2], 2: [1], 3: [4], 4: [3]})

    def test_dot_conversion(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as input_file:
            input_file.write("1, 2\n")
            input_file.write("3, 1\n")
            input_file.write("2, 4\n")
            input_file_name = input_file.name

        convert_to_dot(input_file_name)

        output_file_name = input_file_name.replace('.txt', '.dot')
        with open(output_file_name, 'r') as output_file:
            content = output_file.read()
            expected_content = "digraph {\n1 -> 2\n1 -> 3\n2 -> 1\n2 -> 4\n3 -> 1\n4 -> 2\n}"
            self.assertEqual(content, expected_content)

unittest.main(verbosity=2)
