# python-cloudrun-test

## 初期化

```
python -m vnev venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## デプロイ

### そのままデプロイ

コマンドラインで設定したいときに利用

```
gcloud run deploy --source .
```

### Cloud Buildでデプロイ

```
gcloud builds submit --config=cloudbuild.yaml --region=asia-northeast1
```

### トリガーの設定

- IAM: Cloud Build 編集者
- 予めリポジトリとCloud Buildの連携を許可する必要あり
- コンソール画面で確認する場合「リージョン」に注意