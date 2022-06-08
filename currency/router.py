from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from currency.services import get_data
from database import get_db

from fastapi.security import OAuth2PasswordRequestForm

from user.auth import get_current_user

router = APIRouter()


@router.get('/get_currencies')
async def main(amount: int, db: Session = Depends(get_db),
               form_data: OAuth2PasswordRequestForm = Depends(get_current_user)):
    data = get_data(amount)

    return {"Success": "true",
            'timestamp': data[0],
            'message': {
                "USD": data[1],
                "EUR": data[2]
            }
            }
