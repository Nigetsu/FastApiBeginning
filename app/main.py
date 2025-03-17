from fastapi import FastAPI
from app.cultivators.router import router as router_cultivators
from app.ranks.router import router as router_ranks
from app.position.router import router as router_position
from app.users.router import router as router_users

app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет!"}


app.include_router(router_users)
app.include_router(router_cultivators)
app.include_router(router_ranks)
app.include_router(router_position)
