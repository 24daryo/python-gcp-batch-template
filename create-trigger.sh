#!/bin/bash
source ./.env

# prodにpushしたらデプロイするトリガーを作成
# branch-patternを指定しているの、そのファイルにpushしてデプロイ
# or --tag-pattern=TAG_PATTERN
# キーの詳細：https://cloud.google.com/sdk/gcloud/reference/beta/builds/triggers/create/github
gcloud beta builds triggers create github \
    --name=$CBT_TRIGGER_NAME \
    --description=$CBT_TRIGGER_DESCRIPTION \
    --region=$CBT_REGION \
    --repo-name=$CBT_REPO_NAME \
    --repo-owner=$CBT_REPO_OWNER \
    --branch-pattern=$CBT_BRANCH_PATTERN \
    --build-config=$CBT_BUILD_CONFIG_FILE \
    --include-logs-with-status \
    --substitutions \
_CR_SERVICE_NAME=$CR_SERVICE_NAME,\
_CR_REGION=$CR_REGION,\
_CLOUD_SQL_USER=$CLOUD_SQL_USER,\
_CLOUD_SQL_PASSWORD=$CLOUD_SQL_PASSWORD,\
_CLOUD_SQL_NAME=$CLOUD_SQL_NAME,\
_CLOUD_SQL_INSTANCE=$CLOUD_SQL_INSTANCE