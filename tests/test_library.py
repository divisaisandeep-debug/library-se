import unittest
from src.library import Library

class TestSprint1(unittest.TestCase):

    def test_add_book_success(self):
        library = Library()
        library.add_book(1, "Python", "Author")
        self.assertIn(1, library.books)

    def test_duplicate_book_id(self):
        library = Library()
        library.add_book(1, "Python", "Author")
        with self.assertRaises(ValueError):
            library.add_book(1, "Python", "Author")

if __name__ == "__main__":
    unittest.main()
