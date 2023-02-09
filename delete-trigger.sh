#!/bin/bash
source ./.env
gcloud beta builds triggers delete $CBT_TRIGGER_NAME --region=$CBT_REGION