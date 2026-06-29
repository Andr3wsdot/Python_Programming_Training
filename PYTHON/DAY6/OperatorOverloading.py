print(20+20)
print(("Hello"+"Guys")*4)


class Book:
    def __init__(self,pages):
        self.pages=pages


        def __add__(self,other):
            return self.pages+other.pages
        
h2=Book(290)
h1=Book(100)
print(h1+h2)        