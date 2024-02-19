class Author:

    all = []

    def __init__(self,name):
        self.name = name

    def add_contracts(self, book):
        Contract(self, book)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self ]

    def books(self):
        return [contract.book for contract in self.contracts()]

class Book:

    all = []
    
    def __init__(self,title):
        self.title = title

    def contracts(self):
        return [ contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

    def add_author(self, author):  
        Contract(author, self)

class Contract:

    all = []
    
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author) and isinstance(book, Book) and isinstance(date, str) and isinstance(royalties, int):
            self.author = author
            self.book = book
            self.date = date
            self.royalties = royalties
            Contract.all.append(self)
        else:
            raise Exception


        
        
        

    