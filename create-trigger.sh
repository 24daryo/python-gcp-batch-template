#!/bin/bash
source ./.env

# prodにpushしたらデプロイするトリガーを作成
# branch-patternを指定しているの、そのファイルにpushしてデプロイ
# or --tag-pattern=TAG_PATTERN
# キーの詳細：https://cloud.google.com/sdk/gcloud/reference/beta/builds/triggers/create/github
echo gcloud beta builds triggers create github \
    --name=$CBT_TRIGGER_NAME \
    --description="$CBT_TRIGGER_DESCRIPTION" \
    --region=$CBT_REGION \
    --repo-name=$CBT_REPO_NAME \
    --repo-owner=$CBT_REPO_OWNER \
    --branch-pattern=$CBT_BRANCH_PATTERN \
    --build-config=$CBT_BUILD_CONFIG_FILE \
    --include-logs-with-status \
    --substitutions \
_CLOUD_SQL_USER=$CLOUD_SQL_USER,\
_CLOUD_SQL_PASSWORD=$CLOUD_SQL_PASSWORD,\
_CLOUD_SQL_NAME=$CLOUD_SQL_NAME,\
_CLOUD_SQL_INSTANCE=$CLOUD_SQL_INSTANCE,\
_CRJ_SERVICE_NAME=$CRJ_SERVICE_NAME,\
_CRJ_REGION=$CRJ_REGION,\
_CRJ_MAX_RETRIES=$CRJ_MAX_RETRIES,\
_CRJ_CPU=$CRJ_CPU,\
_CRJ_MEMORY=$CRJ_MEMORY,\
_CRJ_TASK_TIMEOUT=$CRJ_TASK_TIMEOUT,\
_CRJ_PARALLELISM=$CRJ_PARALLELISM,\
_CRJ_TASKS=$CRJ_TASKS,\
_LINE_NOTIFY_TOKEN=$LINE_NOTIFY_TOKEN,\
_CS_JOB_NAME=$CS_JOB_NAME,\
_CS_SCHEDULE="${CS_SCHEDULE}",\
_CS_HTTP_METHOD=$CS_HTTP_METHOD,\
_CS_LOCATION=$CS_LOCATION