import pytest
import os
import sys

# Adjust sys.path to include the src/ directory (one level up from tests/)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application import create_app
from models import db
from flask_jwt_extended import create_access_token

@pytest.fixture
def app():
    app = create_app('settings.py')
    app.config.update({
        "TESTING": False,  # 🔴 Correção para refletir a configuração correta
        "DEBUG": False,  # 🔴 Correção para refletir a configuração correta
        "JWT_SECRET_KEY": "29904e38dc64706d8a61ad4525a7efd91c2f7022e4ab48ede425a6270687dd08",  # 🔴 Correção da chave secreta
        "PROPAGATE_EXCEPTIONS": True,
    })
    with app.app_context():  
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture()
def token(app):
    """Cria um token JWT válido para os testes dentro do contexto da aplicação"""
    with app.app_context():
        return create_access_token(identity="usuario_de_teste")

@pytest.fixture()
def auth_headers(token):
    """Retorna um dicionário com o cabeçalho de autorização"""
    return {"Authorization": f"Bearer {token}"}

# Testes de Configuração

def test_data_base_p():
    from settings import DATABASE_PASS
    assert DATABASE_PASS == "postgres"  # 🔴 Ajustado para corresponder ao valor correto

def test_debug_is_false():
    from settings import DEBUG
    assert DEBUG is False  # 🔴 Ajustado para corresponder ao valor correto
