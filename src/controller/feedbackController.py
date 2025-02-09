from fastapi import APIRouter
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from starlette.responses import JSONResponse
from src.domain.models.feedbackSchema import FeedbackSchema
import os
from dotenv import load_dotenv

feedback = APIRouter(
    prefix="/feedback"
)

load_dotenv()

MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
MAIL_FROM = os.getenv("MAIL_FROM")
MAIL_PORT = os.getenv("MAIL_PORT")
MAIL_SERVER = os.getenv("MAIL_SERVER")
MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME")

conf = ConnectionConfig(
    MAIL_USERNAME=MAIL_USERNAME,
    MAIL_PASSWORD=MAIL_PASSWORD,
    MAIL_FROM=MAIL_FROM,
    MAIL_PORT=MAIL_PORT,
    MAIL_SERVER=MAIL_SERVER,
    MAIL_FROM_NAME=MAIL_FROM_NAME,
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)

@feedback.post("/email")
async def send_feedback_email(feedback_data: FeedbackSchema) -> JSONResponse:
    html = f"""
    <html>
    <head></head>
    <body>
        <h1>Feedback: {feedback_data.tema}</h1>
        <p>Descrição: {feedback_data.descricao}</p>
        <p>Email para Contato: {feedback_data.email_contato}</p>
    </body>
    </html>
    """

    message = MessageSchema(
        subject="Novo Feedback Recebido",
        recipients=feedback_data.recipients,
        body=html,
        subtype=MessageType.html
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "Feedback enviado com sucesso!"})
