import typing
import strawberry
from data_source import get_books

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)
    

schema = strawberry.Schema(query=Query)
