from fastapi import FastAPI
from urls import sign_language_detection_router

app = FastAPI()

app.include_router(sign_language_detection_router)
