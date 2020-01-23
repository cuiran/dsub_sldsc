#!/usr/bin/env python

import subprocess
import os
import sys

#assign variables
BED = os.environ['BED'] # bed file name
BIM = os.environ['BIM'] # bim file prefix
OUT = os.environ['OUT'] # annotation file prefix
PATH = '/home/pyscripts/'

#make directories
subprocess.call(['mkdir','/mnt/data/result/'])
subprocess.call(['mkdir','/mnt/data/bim/'])
subprocess.call(['mkdir','/mnt/data/bed/'])

#copy data
subprocess.call(['gsutil','cp','gs://regularized_sldsc/data/datasets/baselineLD_v2.2/'+BED,'/mnt/data/bed/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/reference_files/UKBB/plink_files/imputed_qc/ukb_imp_v3_5K.*.bim','/mnt/data/bim/'])

#run script
cell_name = BED[:-4]
for i in range(1,23):
    chrom = str(i)
    return_code = subprocess.call(['python',PATH+'make_annot.py',
        '--bed-file','/mnt/data/bed/'+BED,
        '--bimfile','/mnt/data/bim/'+BIM+chrom+'.bim',
        '--annot-file','/mnt/data/result/'+OUT+chrom+'.annot.gz'])
    if return_code != 0:
        sys.exit(1)

subprocess.call(['gsutil','-m','cp','/mnt/data/result/*','gs://regularized_sldsc/data/annot_and_ldscore/UKBB/baselineLD_v2.2/'])
