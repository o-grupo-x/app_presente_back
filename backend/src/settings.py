import os
from dotenv import load_dotenv
from datetime import timedelta

load_dotenv()

# -*- coding: utf-8 -*-
DATABASE_LOGIN = os.environ.get('POSTGRES_USER', 'postgres')
DATABASE_PASS = os.environ.get('POSTGRES_PASSWORD', 'Vkhn2W3LudKzzis')  # Match GitHub Actions
DATABASE_IP = os.environ.get('DATABASE_IP', 'localhost')  # Default to localhost for tests

# Flask core settings
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
TESTING = os.environ.get('TESTING', 'False') == 'True'
SECRET_KEY = os.environ.get('SECRET_KEY', 'qualquercoisa')
PERMANENT_SESSION_LIFETIME = 60 * 60 * 24 * 30
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=3)
OIDC_CLIENT_SECRETS = 'client_secrets_prod.json'
OIDC_OPENID_REALM = 'app-presente'
OIDC_ID_TOKEN_COOKIE_SECURE = False
OIDC_SCOPES = 'openid'
HANDLER = "StreamHandler"

# Flask-WTF settings
WTF_CSRF_ENABLED = os.environ.get('WTF_CSRF_ENABLED', 'True') == 'True'

# Flask-SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DATABASE_LOGIN}:{DATABASE_PASS}@{DATABASE_IP}/app_presente'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Redis settings
REDIS_HOST = os.environ.get('REDIS_HOST', '35.202.222.14')
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', 'redis')

# Flask-Session settings
SESSION_TYPE = 'redis'
SESSION_PERMANENT = False
SESSION_USE_SIGNER = os.environ.get('DEBUG', 'False') == 'False'  # Enable signing in production (when DEBUG=False)
SESSION_KEY_PREFIX = 'session:'
SESSION_REDIS = None  # Initialized in create_app