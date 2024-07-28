import typing
import strawberry
from data_source import get_books
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Book:
    title: str
    author: str

@strawberry.type
class Query:
    """_summary_

    Returns:
        _type_: _description_
    """
    #books: typing.List[Book] = strawberry.field(resolver=get_books)
    @strawberry.field
    def example(self, info: strawberry.Info) -> str:
        return f"Hello {info.context['custom_value']}"
    
schema = strawberry.Schema(query=Query)