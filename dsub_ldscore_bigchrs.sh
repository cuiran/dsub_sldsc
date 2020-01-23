#!/bin/bash

dsub \
    --provider google-v2 \
    --project finucane-dp5 \
    --zone "us-central1-*" \
    --disk-size 100 \
    --logging gs://regularized_sldsc/logging/ABC/ldscore_1000G/ \
    --machine-type n1-standard-4 \
    --image "gcr.io/finucane-dp5/sldsc:latest" \
    --script "run_ldscore.py" \
    --task "submit_ldscore_bigchrs.tsv"
