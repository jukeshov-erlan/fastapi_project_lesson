from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from schemas import *
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Database is clean")
    await create_tables()
    print("Database is ready")
    yield
    print("Power off")

app = FastAPI(lifespan=lifespan) 
app.include_router(tasks_router)




