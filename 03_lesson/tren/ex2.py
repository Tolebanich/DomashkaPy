from book import Book

library = [
    Book("Война и мир", "Лев Толстой"),
    Book("Преступление и наказание", "Фёдор Достоевский"),
    Book("Троецарствие", "Ло Гуанджун")
]

for book in library:
    print(f"{book.name} - {book.author}")