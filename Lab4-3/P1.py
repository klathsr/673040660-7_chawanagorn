"""
Chawanagorn Thiangsiri
673040660-7
Lab4-3 P1
"""
from Library import LibraryItem,Book,TextBook,Magazine

book = Book("Harry Potter", "B001", "J.K. Rowling")
book.set_page_count(500)
book.check_out()
book.display_info()

print("\nTesting TextBook:")
textbook = TextBook("Math", "T1", "ronaldo", "Math", "Grade 1")
textbook.set_page_count(300)
textbook.display_info()
textbook.check_out()
textbook.display_info()

print("\nTesting Magazine:")
magazine = Magazine("football", "cr7", "Lm10")
magazine.display_issue() 
magazine.check_out()
magazine.display_issue() 
        