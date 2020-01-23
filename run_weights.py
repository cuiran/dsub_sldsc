#!/usr/bin/env python2

import subprocess
import os
import sys

#assign variables
BFILE = os.environ['BFILE'] # eg: 1000G.EUR.QC.
ANNOT = os.environ['ANNOT'] # annot file prefix eg: cell1.
OUT = os.environ['OUT'] #ldscore file prefix without chrom eg: cell1.
CHR = os.environ['CHR']
SNPS = '/mnt/data/snp/ukb_v3.'+CHR+'.snp' # print snp file prefix
PATH = '/home/pyscripts/'

#make directories
subprocess.call(['mkdir','/mnt/data/bfile/'])
subprocess.call(['mkdir','/mnt/data/annot/'])
subprocess.call(['mkdir','/mnt/data/snp/'])
subprocess.call(['mkdir','/mnt/data/result/'])

#copy data
subprocess.call(['gsutil','cp','gs://regularized_sldsc/data/reference_files/UKBB/plink_files/imputed_qc_info09_maf10-4/ukb_v3.'+CHR+'.snp','/mnt/data/snp/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/reference_files/UKBB/plink_files/imputed_qc/'+BFILE+CHR+'.*','/mnt/data/bfile/'])
subprocess.call(['gsutil','cp','gs://regularized_sldsc/ABC/data/weights/'+ANNOT+CHR+'*','/mnt/data/annot/'])

#run script
return_code = subprocess.call(['python2',PATH+'ldsc.py',
        '--l2',
        '--bfile','/mnt/data/bfile/'+BFILE+CHR,
        '--ld-wind-cm','1',
        '--annot','/mnt/data/annot/'+ANNOT+CHR+'.annot.gz',
        '--thin-annot',
        '--out','/mnt/data/result/'+OUT+CHR,
        '--print-snps',SNPS])

if return_code!=0:
    sys.exit(1)

subprocess.call(['gsutil','-m','cp','/mnt/data/result/*','gs://regularized_sldsc/ABC/data/weights/'])
