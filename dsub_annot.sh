#!/bin/bash

dsub \
    --provider google-v2 \
    --project finucane-dp5 \
    --zone "us-east1-b" \
    --disk-size 100 \
    --logging gs://regularized_sldsc/logging/ABC/make_annot_1000G/ \
    --machine-type n1-standard-4 \
    --image "gcr.io/finucane-dp5/sldsc:latest" \
    --script "run_make_annot.py" \
    --task "submit_make_annot.tsv"
