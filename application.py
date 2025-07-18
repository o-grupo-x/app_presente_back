from flask import Flask
from flask_cors import CORS
from models import login_manager, db
from flask_session import Session
import redis
import logging
from json_log_formatter import JSONFormatter
import warnings
from sqlalchemy import exc as sqlalchemy_exc

class CustomJSONFormatter(JSONFormatter):
    def json_record(self, message, extra, record):
        extra['log.level'] = record.levelname.lower()
        extra['@timestamp'] = self.format_time(record.created)
        extra['log.logger'] = record.name
        extra['log.origin'] = {
            'function': record.funcName,
            'file.name': record.pathname,
            'file.line': record.lineno,
        }
        extra['message'] = record.getMessage()
        extra['service.name'] = 'flask_app'
        extra['ecs.version'] = '1.6.0'
        return extra

def create_app(config_file='settings.py'):
    warnings.filterwarnings("ignore", category=DeprecationWarning, module="sqlalchemy")

    from flask_login import LoginManager
    from blueprints.AlunoBlueprint import alunos
    from blueprints.ChamadaBlueprint import chamadas
    from blueprints.LembreteBlueprint import lembretes
    from blueprints.PainelBlueprint import paineis
    from blueprints.PresencaBlueprint import presencas
    from blueprints.ProfessorBlueprint import professores
    from blueprints.SecretariaBlueprint import secretaria
    from blueprints.MateriaBlueprint import materias
    from blueprints.TurmaBlueprint import turmas
    from blueprints.UsuarioBlueprint import usuarios
    from blueprints.ConfiguracaoBlueprint import configuracoes
    from flask_wtf.csrf import CSRFProtect
    from flask_jwt_extended import JWTManager

    app = Flask(__name__)
    # Specify allowed origins, methods, and headers
    CORS(app, resources={
        r"/api/*": {
            "origins": ["http://127.0.0.1:*", "http://localhost:*", "https://app.odeiojava.com.br", "http://35.223.77.94"],
            "methods": ["GET", "POST", "OPTIONS"],
            "allow_headers": ["Content-Type", "Authorization"]
        }
    })

    # Logging setup
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler("backend.log"),
            logging.StreamHandler()
        ]
    )

    formatter = CustomJSONFormatter()
    json_handler = logging.FileHandler('backend.log')
    json_handler.setFormatter(formatter)
    json_logger = logging.getLogger('json_logger')
    json_logger.addHandler(json_handler)
    json_logger.setLevel(logging.INFO)

    # Load config
    app.config.from_pyfile(config_file)

    # Initialize Redis for Flask-Session with connection check
    try:
        redis_client = redis.Redis(
            host=app.config['REDIS_HOST'],
            port=app.config['REDIS_PORT'],
            decode_responses=True
            # password=app.config.get('REDIS_PASSWORD'),
        )
        redis_client.ping()
        app.logger.info(f"Successfully connected to Redis at {app.config['REDIS_HOST']}:{app.config['REDIS_PORT']}")
    except redis.ConnectionError as e:
        app.logger.error(f"Failed to connect to Redis: {str(e)}")
        raise

    # Configure Flask-Session
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_PERMANENT'] = False
    app.config['SESSION_USE_SIGNER'] = True
    app.config['SESSION_KEY_PREFIX'] = 'session:'
    app.config['SESSION_REDIS'] = redis_client

    # Initialize session
    Session(app)

    # Initialize extensions
    JWTManager(app)
    db.init_app(app)
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(alunos)
    app.register_blueprint(chamadas)
    app.register_blueprint(lembretes)
    app.register_blueprint(paineis)
    app.register_blueprint(presencas)
    app.register_blueprint(professores)
    app.register_blueprint(secretaria)
    app.register_blueprint(materias)
    app.register_blueprint(turmas)
    app.register_blueprint(usuarios)
    app.register_blueprint(configuracoes)

    app.logger.info('Aplicativo inicializado com sucesso.')
    return app