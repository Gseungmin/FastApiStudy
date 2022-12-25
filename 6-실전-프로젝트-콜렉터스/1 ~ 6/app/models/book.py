from odmantic import Model


class BookModel(Model):
    keyword: str
    publisher: str
    price: int
    image: str

    class Config:
        collection = "books"

# mongoDB는 DB안에 Collection(books)이 존재
# Collection 안에 document(keyword, publisher, price)가 존재