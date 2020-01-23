#!/bin/bash

dsub \
    --provider google-v2 \
    --project finucane-dp5 \
    --zones "us-east1-b" \
    --disk-size 100 \
    --logging gs://regularized_sldsc/logging/ABC/format_ss/ \
    --machine-type n1-standard-4 \
    --image "gcr.io/finucane-dp5/sldsc:latest" \
    --script "run_munge_ss.py" \
    --task "submit_munge_ss.tsv"
