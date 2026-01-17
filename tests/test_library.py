class Library:
    def __init__(self):
        self.books = {}  # book_id -> {title, author, status}

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            raise ValueError("Book ID already exists")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "status": "Available"
        }

    def borrow_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")
        if self.books[book_id]["status"] == "Borrowed":
            raise ValueError("Book already borrowed")
        self.books[book_id]["status"] = "Borrowed"

    def return_book(self, book_id):
        if book_id not in self.books:
            raise ValueError("Book not found")
        self.books[book_id]["status"] = "Available"
    def test_report_contains_header(self):
        report = self.lib.generate_report()
        self.assertIn("BookID | Title | Author | Status", report)

    def test_report_contains_book_entry(self):
        report = self.lib.generate_report()
        self.assertIn("B1", report)

