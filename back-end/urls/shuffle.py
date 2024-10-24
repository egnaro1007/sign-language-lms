from fastapi import APIRouter, Query
from models.shuffle import ShuffleQuestion
from typing import Optional

shuffle_question_router = APIRouter(prefix="/shuffle")

@shuffle_question_router.get("/question/{id}")
def get_question(id: Optional[int] = None):
    question = ShuffleQuestion()
    if id is None:
        question.load_from_database()
    else:
        question.load_from_database(id)
    return question.get_subsequents()

@shuffle_question_router.get("/questions")
def get_random_questions(number: int = Query(..., gt=0)):
    return_list = []
    for _ in range(number):
        question = ShuffleQuestion()
        question.load_random_from_database()
        return_list.append(question.get_subsequents())

    return return_list
