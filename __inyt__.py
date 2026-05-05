from contextlib import asynccontextmanager
from fastapi import FastAPI 

@asynccontextmanager
async def lifespan(_:FastAPI):
    app=FastAPI(
        title="todo API",
        description="API para gerenciamento de tarefas com arquitetura em camadas.",
        version="1.0.0"
        lifespan=lifespan,
        contact={
            "name": "equipe da disciplina INF8B",
        }, )

    return app
    