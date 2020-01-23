#!/usr/bin/env python2

import subprocess
import os
import pandas as pd
import sys

#assign variables
SUMSTAT = os.environ['SUMSTAT']
OUT = os.environ['OUT']
NCASE = os.environ['NCASE']
NCON = os.environ['NCON']
PATH = '/home/pyscripts/' #default ldsc path

#make directories
subprocess.call(['mkdir','/mnt/data/ss/'])
subprocess.call(['mkdir','/mnt/data/result/'])

#copy data
ss_name = os.path.basename(SUMSTAT)
subprocess.call(['gsutil','cp','gs://regularized_sldsc/ABC/data/iibdgc-trans-ancestry-filtered-summary-stats/'+ss_name,'/mnt/data/ss/'])

#assign variant ID
df = pd.read_csv('/mnt/data/ss/'+ss_name,delim_whitespace=True)
#df['SNP'] = df['CHR'].astype(str)+':'+df['BP'].astype(str)+':'+df['A1']+':'+df['A2']
l = [list(x) for x in df['Direction'].tolist()]
df['sign'] = [x.count('+') - x.count('-') for x in l]
if df[df['sign']==0].shape[0]/df.shape[0] >=0.5:
    raise ValueError('Too many zeros in sign')
df.to_csv('/mnt/data/ss/'+ss_name,sep='\t',index=False)

#run script
return_code = subprocess.call(['python2',PATH+'munge_sumstats.py',
    '--sumstats',SUMSTAT,
    '--N-cas', NCASE,
    '--N-con',NCON,
    '--out', OUT,
    '--a1','A1',
    '--a2','A2',
    '--p','P',
    '--signed-sumstats','sign,0'])
if return_code!=0:
    sys.exit(1)

subprocess.call(['gsutil','cp','/mnt/data/result/*','gs://regularized_sldsc/ABC/data/formatted_sumstats_rsid/'])
