import os
from dotenv import load_dotenv
from datetime import timedelta
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

# Database settings
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql+psycopg2://postgres:Vkhn2W3LudKzzis@localhost/app_presente')
logger.info(f"Using SQLALCHEMY_DATABASE_URI: {SQLALCHEMY_DATABASE_URI}")
SQLALCHEMY_TRACK_MODIFICATIONS = False

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

WTF_CSRF_ENABLED = os.environ.get('WTF_CSRF_ENABLED', 'True') == 'True'

REDIS_HOST = '34.118.230.117'
REDIS_PORT = int(os.environ.get('REDIS_PORT', 6379))
REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', 'redis')

SESSION_TYPE = 'redis'
SESSION_PERMANENT = False
SESSION_USE_SIGNER = os.environ.get('DEBUG', 'False') == 'False'
SESSION_KEY_PREFIX = 'session:'
SESSION_REDIS = None
