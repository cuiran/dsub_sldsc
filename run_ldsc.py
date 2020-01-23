#!/usr/bin/env python2

import subprocess
import os
import sys

#assign variables
SUMSTAT = os.environ['SUMSTAT'] # name of the sumstats file
GS_SS = os.environ['GSSS'] # path in bucket of parent directory for sumstats file
REFLD = os.environ['REFLD'] # reference ld file prefix eg: baseline.
GS_RLD = os.environ['GSRLD'] # path in bucket of parent directory for reference ld file
OUT = os.environ['OUT'] # output prefix
PATH = '/home/pyscripts/'

#make directories
subprocess.call(['mkdir','/mnt/data/ss/'])
subprocess.call(['mkdir','/mnt/data/refld/'])
subprocess.call(['mkdir','/mnt/data/ctsld/'])
subprocess.call(['mkdir','/mnt/data/result/'])

#copy data
subprocess.call(['gsutil','cp',GS_SS+SUMSTAT,'/mnt/data/ss/'])
subprocess.call(['gsutil','-m','cp',GS_RLD+REFLD+'*.ldscore.gz','/mnt/data/refld/'])
subprocess.call(['gsutil','-m','cp',GS_RLD+REFLD+'*.M','/mnt/data/refld/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/ABC/data/annot_1000G_rsid/*.gz','/mnt/data/ctsld/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/ABC/data/annot_1000G_rsid/*.M','/mnt/data/ctsld/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/ABC/data/annot_1000G_rsid/ABC_dsub.ldcts','/mnt/data/ctsld/'])

#run script
return_code = subprocess.call(['python2',PATH+'ldsc.py',
        '--h2-cts', '/mnt/data/ss/'+SUMSTAT,
        '--ref-ld-chr', '/mnt/data/refld/'+REFLD,
        '--out', '/mnt/data/result/'+OUT,
        '--ref-ld-chr-cts', '/mnt/data/ctsld/ABC_dsub.ldcts',
        '--not-M-5-50',
        '--overlap-annot',
        '--w-ld-chr', '/mnt/data/ctsld/weights.'])

if return_code != 0:
    sys.exit(1)

subprocess.call(['gsutil','-m','cp','/mnt/data/result/*','gs://regularized_sldsc/ABC/results/s-ldsc/NOV-2019-1000G-rsid/'])
