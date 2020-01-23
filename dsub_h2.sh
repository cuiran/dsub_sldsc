#!/bin/bash

dsub \
    --provider google-v2 \
    --project finucane-dp5 \
    --zone "us-east1-*" \
    --disk-size 100 \
    --logging gs://regularized_sldsc/logging/ABC/s-ldsc_1000G_sep/ \
    --machine-type n1-highmem-16 \
    --image "gcr.io/finucane-dp5/sldsc:latest" \
    --script "run_ldsc_sep.py" \
    --task "submit_ldsc_joint.tsv"
