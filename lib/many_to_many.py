class Author:
    
    def __init__(self,name):
        self.name = name


class Book:
    
    def __init__(self,title):
        self.title = title


class Contract:
    
    def __init__(self, author, book, date, royalties):
        # validate that type author == author
        if isinstance(author, Author) and isinstance(book, Book) and isinstance(self.date, str):
            self.author = author
            self.book = book
            self.date = date
        else:
            raise Exception
        
        
        self.royalties = royalties

    