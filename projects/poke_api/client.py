from typing import Union
from fastapi import FastAPI, Depends, Request, WebSocket, BackgroundTasks
from pydantic import BaseModel
from strawberry.fastapi import GraphQLRouter
from schema import schema

app = FastAPI()

class Item(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_rood():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None) -> object:
    """_summary_

    Args:
        item_id (int): _description_
        q (Union[str, None], optional): _description_. Defaults to None.

    Returns:
        object: _description_
    """
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    """_summary_

    Args:
        item_id (int): _description_
        item (Item): _description_

    Returns:
        _type_: _description_
    """
    return {"item_price": item.price, "item_id": item_id, "item_name": item.name}


def custom_context_dependency() -> str:
    return "John"


async def get_context(
        custom_value=Depends(custom_context_dependency),
):
    return {
        "custom_value": custom_value
    }


graphql_app = GraphQLRouter(schema,
                            context_getter=get_context)

app.include_router(graphql_app, prefix="/graphql")
