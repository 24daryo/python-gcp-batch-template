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
_DB_USER=$DB_USER,\
_DB_PASSWORD=$DB_PASSWORD,\
_DB_NAME=$DB_NAME,\
_CR_CLOUNDSQL_INSTANCE=$CR_CLOUNDSQL_INSTANCE