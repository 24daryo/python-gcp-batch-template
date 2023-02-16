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
    # Storageのクライアントを作成
    DB_URI = f'postgresql://{USER}:{PASS}@{DB_HOST}:{DB_PORT}/{NAME}'
else:
    DB_URI = f"postgresql+psycopg2://{USER}:{PASS}@/{NAME}?host={UNIX_SOCKET}"

# Storage
if IS_LOCAL:
    path = '/'+os.getenv('LOCAL_STORAGE_SERVICE_ACCOUNT_KEY_PATH', "")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = path
CLOUD_STORAGE_BUCKET = os.getenv('CLOUD_STORAGE_BUCKET')

# ==============
# Messaging
# ==============
LINE_NOTIFY_TOKEN=os.getenv('LINE_NOTIFY_TOKEN', '')
FROM_EMAIL=os.getenv('FROM_EMAIL', '') # 送信元メールアドレス
FROM_PASSWORD=os.getenv('FROM_PASSWORD', '') # 送信元パスワード(2段階認証プロセスを利用してアプリパスワード入力)
TO_EMAIL=os.getenv('TO_EMAIL', '') # 送信先メールアドレス