# python-gcp-batch-test

`Python[flask]` + `Docker` + `GCP[Run,Build,SQL,Storage]`

Python用バッチ処理テンプレート

![](./docs/diagrams.drawio.svg)

### 特徴

1. 変数を設定は`.env`のみで完結
2. GithubへPushして自動デプロイするCloud Buildの利用
3. シェルスクリプトでCloud Build Triggerを簡単に設定可能

## 初期設定

### Cloud Scheduler API用の権限付きサービスアカウント作成

oidc-service-account-email

### 1. `.env`の用意

変数名はそのままかつ`=`にスペースを空けず、任意の変数を設定します
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
# Cloud Run
# ====================
# CloudRunのサービス名
CR_SERVICE_NAME=''
# CloudRunのリージョン
CR_REGION=''

# ====================
# Cloud Build Trigger
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

A. 記述済みの`create-trigger.sh`から処理を呼び出します

```
bash create-trigger.sh
```

B. トリガーを削除する場合は`delete-trigger.sh`を用います

```
bash delete-trigger.sh
```

C. トリガーに失敗する時

- IAM: Cloud Build 編集者
- 予めリポジトリとCloud Buildの連携を許可する必要あり
- コンソール画面で確認する場合「リージョン」に注意

### 3. デプロイ

`cloudbuild.yaml`により設定したブランチへpushすると、自動的にデプロイされます


##　ローカルでの開発

### 1. venv構築

```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

> docker-composeを用いるので、インテリセンス以外では不要

### 2. GCP用のサービスアカウントキーを設定

credentialsフォルダに格納し、それに合わせたenvにします

### 3. `docker-compose.yaml`の起動

```
docker compose up --build
```

> 事前のDockerインスストールが必要


一旦ローカルで試してみる