from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def getall():
    return {'pokémons': 'all pokemons'}


@app.get('/pokemon/{id}')
async def get_by_id(poke_id: int):
    return {'pokemon': poke_id}
