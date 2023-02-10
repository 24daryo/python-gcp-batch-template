# python-gcp-batch-test

## 初期設定

### 1. `.env`の用意

```py
# ====================
# Local Docker Compose Setting(手元で開発するのに必要)
# ====================
PORT='8080'
LOCAL_SQL_PROXY_PATH='credentials/~~~.json'
LOCAL_DB_HOST='db'
LOCAL_DB_PORT='5432'

# ====================
# Cloud SQL
# ====================
CLOUD_SQL_USER=''
CLOUD_SQL_PASSWORD=''
CLOUD_SQL_NAME=''
CLOUD_SQL_INSTANCE='~~~:---:~~~'

# ====================
# CloudBuild
# ====================
# CloudRunのサービス名
CR_SERVICE_NAME='2'
# CloudRunのリージョン
CR_REGION=''


# ====================
# CloudBuildTrigger
# キーの詳細：https://cloud.google.com/sdk/gcloud/reference/beta/builds/triggers/create/github
# ====================
# リポジトリオーナーの名前
CBT_REPO_OWNER=""
# リポジトリの名前
CBT_REPO_NAME=""
# ビルドを呼び出すリポジトリ内のブランチ名
CBT_BRANCH_PATTERN="^hoge$"
# CloudBuild構成ファイルの場所
CBT_BUILD_CONFIG_FILE="cloudbuild.yaml"
# トリガー名
CBT_TRIGGER_NAME=""
# トリガーの説明
CBT_TRIGGER_DESCRIPTION=""
# トリガーのリージョン
CBT_REGION=''

```

### 2. トリガーの登録

記述済みの`create-trigger.sh`から処理を呼び出します

```
bash create-trigger.sh
```

トリガーを削除する場合は以下のshellを実行します

```
bash delete-trigger.sh
```

#### 補足. トリガーの設定の注意点

- IAM: Cloud Build 編集者
- 予めリポジトリとCloud Buildの連携を許可する必要あり
- コンソール画面で確認する場合「リージョン」に注意

### 3. デプロイ

`cloudbuild.yaml`により設定したブランチへpushすると、自動的にデプロイされます

##　ローカルでの開発

### 1. vnev構築

※ docker-composeを用いるので、インテリセンス以外では不要

```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. `docker-compose.yaml`の起動

※ 事前のDockerインスストールが必要

```
docker compose up --build
```

##### 補足. `python main.py`ではダメ？

proxyを立ち上げる必要があるためdocker-composeを用います
