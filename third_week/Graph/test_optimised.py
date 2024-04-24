import unittest
import tempfile

from unittest import TestCase
from graph_gemini import get_graph_from_file, to_edge_dict, \
    is_edge_in_graph, add_edge, del_edge, add_node, del_node, convert_to_dot

class GraphTest(TestCase):
    """testing"""
    def test_get_graph_fromcorrect_file(self):
        """Test with a valid file"""
        result = get_graph_from_file("data1.txt")
        self.assertEqual(result, [[1, 2], [3, 4], [1, 5]])

    def test_read_nonexistent_file(self):
        """Checks if the function raises an exception when reading a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            get_graph_from_file("nonexistent.txt")

    def test_empty_edge_list(self):
        """Tests conversion with an empty edge list."""
        edge_list = []
        expected_dict = {}
        self.assertEqual(to_edge_dict(edge_list), expected_dict)

    def test_basic_conversion(self):
        """Tests the basic conversion of a list of edges to a dictionary of vertices."""
        edge_list = [[1, 2], [3, 4], [1, 5], [2, 4]]
        expected_dict = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        self.assertEqual(to_edge_dict(edge_list), expected_dict)

    def test_duplicate_edges(self):
        """Tests if duplicate edges are handled correctly. """
        edge_list = to_edge_dict([[1, 2], [1, 3]])
        expected_dict = {1: [2, 3], 2: [1], 3: [1]}
        self.assertEqual(edge_list, expected_dict)

    def test_existing_edge(self):
        """Tests if an existing edge is correctly identified."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        edge = (1, 2)
        self.assertTrue(is_edge_in_graph(graph, edge))

    def test_non_existing_edge(self):
        """Tests if a non-existing edge is correctly identified."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        edge = (3, 1)  # Edge does not exist
        self.assertFalse(is_edge_in_graph(graph, edge))

    def test_reversed_existing_edge(self):
        """Tests if the function works for reversed edges in an undirected graph."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        edge = (2, 1)  # Existing edge in reversed order
        self.assertTrue(is_edge_in_graph(graph, edge)) 

    def test_missing_node(self):
        """Tests if the function handles missing nodes gracefully."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        edge = (6, 2)  # Node 6 does not exist
        self.assertFalse(is_edge_in_graph(graph, edge))         

    def test_empty_graph(self):
        """Tests if the function handles an empty graph."""
        graph = {}
        edge = (1, 2)
        self.assertFalse(is_edge_in_graph(graph, edge))    

    def test_add_new_edge(self):
        """Tests adding a new edge to a graph."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        new_edge = (1, 3)
        expected_graph = {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
        self.assertEqual(add_edge(graph.copy(), new_edge), expected_graph)
        self.assertTrue(is_edge_in_graph(expected_graph, new_edge))

    def test_add_edge_to_new_node(self):
        """Tests adding an edge where one or both nodes are new."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        new_edge = (6, 7)  # Both nodes are new
        expected_graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1], 6: [7], 7: [6]}
        self.assertEqual(add_edge(graph.copy(), new_edge), expected_graph)
        self.assertTrue(is_edge_in_graph(expected_graph, new_edge))

    def test_delete_existing_edge(self):
        """Tests deleting an existing edge from the graph."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        edge_to_delete = (2, 4)
        expected_graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        self.assertEqual(del_edge(graph.copy(), edge_to_delete), expected_graph)
        self.assertFalse(is_edge_in_graph(expected_graph, edge_to_delete))

    def test_delete_non_existing_edge(self):
        """Tests deleting an edge that does not exist in the graph."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        edge_to_delete = (2, 6)  # Edge does not exist
        expected_graph = graph.copy()  # Graph should remain the same
        self.assertEqual(del_edge(graph.copy(), edge_to_delete), expected_graph)
        self.assertFalse(is_edge_in_graph(expected_graph, edge_to_delete))

    def test_delete_last_edge_from_node(self):
        """Tests deleting the last edge from a node, making it isolated."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        edge_to_delete = (1, 5)
        expected_graph = {1: [2], 2: [1, 4], 3: [4], 4: [2, 3], 5: []}
        self.assertEqual(del_edge(graph.copy(), edge_to_delete), expected_graph)
        self.assertFalse(is_edge_in_graph(expected_graph, edge_to_delete))

    def test_add_new_node(self):
        """Tests adding a new node to the graph."""
        graph = {1: [2], 2: [1]}
        new_node = 3
        expected_graph = {1: [2], 2: [1], 3: []}
        self.assertEqual(add_node(graph.copy(), new_node), expected_graph)

    def test_add_existing_node(self):
        """Tests adding a node that already exists in the graph."""
        graph = {1: [2], 2: [1]}
        existing_node = 2
        expected_graph = graph.copy()  # Graph should remain unchanged 
        self.assertEqual(add_node(graph.copy(), existing_node), expected_graph)

    def test_add_node_to_empty_graph(self):
        """Tests adding a node to an empty graph."""
        graph = {}
        new_node = 5
        expected_graph = {5: []}
        self.assertEqual(add_node(graph, new_node), expected_graph)

    def test_delete_node_with_edges(self):
        """Tests deleting a node that has incident edges."""
        graph = {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
        node_to_delete = 4
        expected_graph = {1: [2, 5], 2: [1], 3: [], 5: [1]}
        self.assertEqual(del_node(graph.copy(), node_to_delete), expected_graph)

        # Ensure edges are removed
        for neighbor in [2, 3]: 
            self.assertFalse(is_edge_in_graph(expected_graph, (neighbor, node_to_delete)))

    def test_delete_isolated_node(self):
        """Tests deleting a node with no incident edges."""
        graph = {1: [2, 5], 2: [1, 4], 3: []}
        node_to_delete = 3
        expected_graph = {1: [2, 5], 2: [1, 4]}
        self.assertEqual(del_node(graph.copy(), node_to_delete), expected_graph)

    def test_delete_non_existing_node(self):
        """Tests deleting a node that does not exist in the graph."""
        graph = {1: [2, 5], 2: [1, 4]}
        node_to_delete = 6
        expected_graph = graph.copy()  # Graph should remain unchanged
        self.assertEqual(del_node(graph.copy(), node_to_delete), expected_graph)

    def test_delete_node_from_empty_graph(self):
        """Tests deleting a node from an empty graph."""
        graph = {}
        node_to_delete = 3
        expected_graph = {} 
        self.assertEqual(del_node(graph.copy(), node_to_delete), expected_graph)

    def test_dot_conversion(self):
        """Tests the conversion of a simple graph to DOT format."""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as input_file:
            input_file.write("1, 2\n")
            input_file.write("3, 1\n")
            input_file.write("2, 4\n")
            input_file_name = input_file.name
        convert_to_dot(input_file_name)
        output_file_name = input_file_name.replace('.txt', '.dot')
        with open(output_file_name, 'r', encoding='utf-8') as output_file:
            content = output_file.read()
            expected_content = "digraph {\n1 -> 2\n1 -> 3\n2 -> 1\n2 -> 4\n3 -> 1\n4 -> 2\n}"
            self.assertEqual(content, expected_content)

unittest.main(verbosity=2)
