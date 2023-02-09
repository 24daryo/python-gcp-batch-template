import os
import dotenv
dotenv.load_dotenv()

SERVER_HOST = os.getenv('SERVER_HOST', '0.0.0.0')
SERVER_PORT = int(os.getenv("PORT", 8080))

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')

INSTANCE_CONNECTION_NAME = os.getenv('CR_CLOUNDSQL_INSTANCE')
INSTANCE_UNIX_SOCKET = f'cloudsql/{INSTANCE_CONNECTION_NAME}'
IS_LOCAL = False if os.environ.get('SQL_PROXY_PATH') is None else True

if IS_LOCAL:
    DB_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
else:
    print("Global!!")
    # DB_URL = f"postgresql+pg8000://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?unix_sock={INSTANCE_UNIX_SOCKET}/.s.PGSQL.5432"
    DB_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@/{INSTANCE_UNIX_SOCKET}/{DB_NAME}"
    # DB_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@/{DB_NAME}?host={INSTANCE_UNIX_SOCKET}"
    print(DB_URI)