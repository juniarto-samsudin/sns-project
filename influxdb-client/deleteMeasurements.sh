#!/bin/bash

current_date=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

./influx delete --bucket sample-bucket --predicate '_measurement="Bitcoin-Prediction"' --start 1970-01-01T00:00:00Z --stop $current_date -c onboarding
./influx delete --bucket sample-bucket --predicate '_measurement="Bitcoin"' --start 1970-01-01T00:00:00Z --stop $current_date -c onboarding
./influx delete --bucket sample-bucket --predicate '_measurement="Bitcoin-Sentiment"' --start 1970-01-01T00:00:00Z --stop $current_date -c onboarding