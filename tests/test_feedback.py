

import pytest
import asyncio
from httpx import AsyncClient
from fastapi.testclient import TestClient
from src.main import app  
from controller import feedbackController.py   


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# Configuração do cliente de teste
client = TestClient(app)



# Mock da função de envio de email para evitar envios reais durante os testes
@pytest.fixture
def mock_send_email(monkeypatch):
    async def mock_send(*args, **kwargs):
        return None

    monkeypatch.setattr(FastMail, "send_message", mock_send)

# Teste para o endpoint /feedback/email
def test_send_feedback_email(mock_send_email):
    # Dados de exemplo para o feedback
    feedback_data = {
        "tema": "Problema no sistema",
        "descricao": "O sistema está lento.",
        "email_contato": "silvaluiza308@gmail.com",
        "recipients": ["admin@example.com"]
    }

    # Fazendo a requisição POST para o endpoint
    response = client.post("/feedback/email", json=feedback_data)

    # Verificando a resposta
    assert response.status_code == 200
    assert response.json() == {"message": "Feedback enviado com sucesso!"}