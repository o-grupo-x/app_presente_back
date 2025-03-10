import pytest
import os
import sys

# Adjust sys.path to include the src/ directory (one level up from tests/)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from application import create_app
from models import db

@pytest.fixture
def app():
    app = create_app('settings_test.py')  # Ensure this points to the correct config file
    app.config.update({
        "TESTING": True,
    })
    # Optional: Set up a test database context if needed
    with app.app_context():
        db.create_all()  # Create tables for testing
        yield app
        db.drop_all()  # Clean up after tests

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()