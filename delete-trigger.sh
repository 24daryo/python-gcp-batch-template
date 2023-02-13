#!/bin/bash
source ./.env
gcloud beta builds triggers delete $CBT_TRIGGER_NAME --region=$CBT_REGION
gcloud beta scheduler jobs delete $CS_JOB_NAME --location=$CS_LOCATION