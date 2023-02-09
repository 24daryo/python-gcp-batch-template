#!/bin/bash
source ./.env

gcloud builds submit \
    --config=cloudbuild_init.yaml \
    --region=$_CR_REGION\
    --substitutions \
        _CR_SERVICE_NAME=$CR_SERVICE_NAME,_CR_REGION=$CR_REGION,_CR_CLOUNDSQL_INSTANCE=$CR_CLOUNDSQL_INSTANCE