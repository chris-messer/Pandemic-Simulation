# Introduction
This code repository is the collection of files for the final report on pandemic simulation. This repository is organized as follows:

## data
**no_mask_no_vacc_10k.csv** This is the simulation output from running the model under the base case assumptions as described in the report.

**50pcnt_vacc_10k.csv** - this is the simulation output from running the model under the alternative assumptions assuming a 50% mean vaccination rate.

## figures
This directory contains the output of figures used in the report.

## report
This directory contains the LaTeX files used on overleaf.com to write the report

## src 
this directory contains the source code for generating and analyzing the data. 

### Analysis.ipynb
This file contains the python notebook code for analyzing the simulation output, generating the figures and statistics noted in the report

### this file contains the simulation source code that allws for generation of the simulation output. 

## miscellaneous files
The remainder of the files in this directory are the gitignored files to remove data from being stored in the reposistory and the env file noting the program dependencies. 