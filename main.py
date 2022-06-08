from fastapi import FastAPI
from currency.router import router as currency_router
from user.router import router as user_router


app = FastAPI()


app.include_router(currency_router)
app.include_router(user_router)