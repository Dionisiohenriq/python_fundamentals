import typing
import strawberry
from strawberry.fastapi import GraphQLRouter, BaseContext
from fastapi import FastAPI, Depends, Request, WebSocket, BackgroundTasks


@strawberry.type
class Book:
    title: str
    author: str


class CustomContext(BaseContext):
    def __init__(self, greeting: str, name: str) -> None:
        self.greeting = greeting
        self.name = name


def get_books():
    return [
        schema.Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
    ]


def custom_context_dependency() -> CustomContext:
    return CustomContext(greeting="you rock!", name="Henrique")


async def get_context(
        custom_context=Depends(custom_context_dependency),
):
    return custom_context


@strawberry.type
class Query:
    @strawberry.field
    def example(self, info: strawberry.Info) -> str:
        return f"Hello {info.context.name}, {info.context}"


schema = strawberry.Schema(query=Query)
