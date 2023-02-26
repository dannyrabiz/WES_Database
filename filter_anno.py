#import packages
import numpy as np  
import pandas as pd 
import concurrent.futures
import os 
import time


#get sample names
samples = pd.read_csv('Concat/samples.txt', sep ='\t', header = None)
samples = list(samples[0])
samples = [i.split('.')[0] for i in samples]

a = time.time()

#header
header = pd.read_csv('nonsyn.myanno.hg19_multianno.txt', sep = '\t', nrows=1).columns
header = list(header[: len(header)-len(samples)]) + samples

#This is probably not the fastest way to do this, but when I tried parallel it didnt help
filtered_df = pd.DataFrame()
chunk_size = 10000
num = 0

for chunk in pd.read_csv('nonsyn.myanno.hg19_multianno.txt', sep = '\t', chunksize=chunk_size, header = None):

    chunk.columns = header
    chunk['SampleIDs'] = chunk.apply(get_sample_ids, axis=1)
    chunk['SampleInfo'] = chunk.apply(get_sample_ids_and_reads, axis=1)
    chunk['SampleCount'] = chunk['SampleIDs'].str.count(',') + 1
    chunk = chunk.drop(columns=samples)
    filtered_df = pd.concat([filtered_df, chunk], ignore_index=True)
    print(num, time.time()-a)
    num+=1

print(time.time()-a)

#Output files
filtered_df.to_csv('Filtered_annotation.txt', sep ='\t', index=False)
cols_to_drop = [13, 14, 15, 25, 26, 27, 28, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]
filtered_df = filtered_df.drop(filtered_df.columns[cols_to_drop], axis=1)
filtered_df.to_excel('Filtered_annotation.xlsx', index=False)
