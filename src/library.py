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
    def generate_report(self):
        report = ["BookID | Title | Author | Status"]
        for book_id, data in self.books.items():
            report.append(
                f"{book_id} | {data['title']} | {data['author']} | {data['status']}"
            )
        return "\n".join(report)

