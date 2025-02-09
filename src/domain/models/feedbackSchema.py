from pydantic import BaseModel, EmailStr
from typing import List

class FeedbackSchema(BaseModel):
    recipients: List[EmailStr]
    tema: str
    descricao: str
    email_contato: str
