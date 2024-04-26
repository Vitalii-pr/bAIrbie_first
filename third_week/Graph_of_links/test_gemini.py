import unittest
import os
from human_correct import build_graph_from_note, convert_to_dot

class TestNotesLink(unittest.TestCase):

    def setUp(self):
        # Create temporary test files
        self.test_files = {
            "note.md": "My favourite note is [[note4]].",
            "note1.md": "[[note.md]]",
            "note2.md": "[[note.md]] [[note1.md]] [[note3.md]]",
            "note3.md": "",
            "note4.md": "[[note.md]]"
        }
        for file_name, content in self.test_files.items():
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(content)

    def tearDown(self):
        # Remove temporary test files
        for file_name in self.test_files.keys():
            os.remove(file_name)

    def test_build_graph_from_note(self):
        # Test case 1: Single note with no links
        graph = build_graph_from_note("note3.md")
        self.assertDictEqual(graph, {})

        # Test case 2: Note linked to another note
        graph = build_graph_from_note("note.md")
        self.assertDictEqual(graph, {"note": ["note4"], "note4": ["note.md"]})

        # Add more test cases as needed

    def test_convert_to_dot(self):
        # Test case: Test conversion to DOT format
        graph = {"note": ["note4"], "note4": ["note"]}
        convert_to_dot(graph)

        # Check if the dot file is created and contains expected content

        # Add more test cases as needed

if __name__ == "__main__":
    unittest.main()