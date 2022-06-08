from pydantic import BaseModel
from typing import List


class CurrencyCreate(BaseModel):
    id: int
    currency_name: str
    exchange_rate: int
    datetime: str


class Currency(BaseModel):
    USD: int
    EUR: int


class CurrencyResponse(BaseModel):
    success: bool = True
    timestamp: str
    message: List[Currency]
