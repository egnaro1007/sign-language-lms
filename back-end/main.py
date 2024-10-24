from database import Database
from models.shuffle import ShuffleQuestion
from fastapi import FastAPI
from urls.shuffle import shuffle_question_router

db = Database("database.db")

app = FastAPI()

app.include_router(shuffle_question_router)
