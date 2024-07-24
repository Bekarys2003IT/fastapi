from typing import Optional, Annotated

from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print("Database is deleted")
    await create_tables()
    print("Database is ready")
    yield
    print("Turn off")
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


