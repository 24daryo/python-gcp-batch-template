import os
import dotenv

dotenv.load_dotenv()

USER = os.getenv('CLOUD_SQL_USER')
PASS = os.getenv('CLOUD_SQL_PASSWORD')
NAME = os.getenv('CLOUD_SQL_NAME')

CONNECTION_NAME = os.getenv('CLOUD_SQL_INSTANCE')
UNIX_SOCKET = f'/cloudsql/{CONNECTION_NAME}'
IS_LOCAL = False if os.environ.get('LOCAL_SQL_PROXY_PATH') is None else True

if IS_LOCAL:
    DB_HOST = os.getenv('LOCAL_DB_HOST')
    DB_PORT = os.getenv('LOCAL_DB_PORT')
    DB_URI = f'postgresql://{USER}:{PASS}@{DB_HOST}:{DB_PORT}/{NAME}'
else:
    # DB_URI = f"postgresql+pg8000://{USER}:{PASSWORD}@/{NAME}?unix_socket={UNIX_SOCKET}/.s.PGSQL.5432"
    DB_URI = f"postgresql+psycopg2://{USER}:{PASS}@/{NAME}?host={UNIX_SOCKET}"