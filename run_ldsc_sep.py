#!/usr/bin/env python2

import subprocess
import os
import sys

#assign variables
SUMSTAT = os.environ['SUMSTAT'] # name of the sumstats file
GS_SS = os.environ['GSSS'] # path in bucket of parent directory for sumstats file
REFLD = os.environ['REFLD'] # reference ld file prefix eg: baseline.
GS_RLD = os.environ['GSRLD'] # path in bucket of parent directory for reference ld file
CELL = os.environ['CELL'] # cell name
GS_BFILE = os.environ['GSBFILE'] # path in bucket of bfiles
BFILE = os.environ['BFILE'] # bfile prefix, e.g.:  1000G.EUR.QC.
OUT = os.environ['OUT'] # output prefix
PATH = '/home/pyscripts/'

#make directories
subprocess.call(['mkdir','/mnt/data/ss/'])
subprocess.call(['mkdir','/mnt/data/frq/'])
subprocess.call(['mkdir','/mnt/data/refld/'])
subprocess.call(['mkdir','/mnt/data/ctsld/'])
subprocess.call(['mkdir','/mnt/data/result/'])

#copy data
subprocess.call(['gsutil','-m','cp',GS_SS+SUMSTAT,'/mnt/data/ss/'])
subprocess.call(['gsutil','-m','cp',GS_BFILE+BFILE+'*.frq','/mnt/data/frq/'])
subprocess.call(['gsutil','-m','cp',GS_RLD+REFLD+'*','/mnt/data/refld/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/ABC/data/annot_1000G_rsid/*','/mnt/data/ctsld/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/ABC/data/annot/*.annot.gz','/mnt/data/ctsld/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/ABC/data/annot_1000G_rsid/weights.*','/mnt/data/ctsld/'])

#run script
return_code = subprocess.call(['python2',PATH+'ldsc.py',
        '--h2', '/mnt/data/ss/'+SUMSTAT,
        '--ref-ld-chr', '/mnt/data/refld/{},{}'.format(REFLD,CELL),
        '--out', '/mnt/data/result/'+OUT,
#        '--overlap-annot',
#        '--frqfile-chr', '/mnt/data/frq/{}'.format(BFILE),
        '--w-ld-chr', '/mnt/data/ctsld/weights.'])

if return_code != 0:
    sys.exit(1)

SS_NAME = '.'.join(SUMSTAT.split('.')[:-2])
subprocess.call(['gsutil','-m','cp','/mnt/data/result/*','gs://regularized_sldsc/ABC/results/s-ldsc/JAN-2020-1000G-rsid-joint/'])
