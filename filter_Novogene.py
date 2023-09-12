#This is SNP only 
import numpy as np 
import pandas as pd 
samples = pd.read_csv('samples.txt', sep ='\n', header = None)
samples = list(samples[0])
keep = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'GeneName',
       'Func', 'Gene', 'GeneDetail', 'ExonicFunc', 'AAChange', 'Gencode',
       'cytoBand', 'genomicSuperDups', 'Repeat', 'avsnp150',
       'cosmic70', 'CLNALLELEID', 'CLNDN', 'CLNDISDB', 'CLNREVSTAT', 'CLNSIG',
       'gnomad_exome_AF', 'gnomad_exome_AF_raw', 'gnomad_exome_AF_afr',
       'gnomad_exome_AF_sas', 'gnomad_exome_AF_amr', 'gnomad_exome_AF_eas',
       'gnomad_exome_AF_nfe', 'gnomad_exome_AF_fin', 'gnomad_exome_AF_asj',
       'gnomad_exome_AF_oth', 'SIFT',
       'Polyphen2_HDIV', 'Polyphen2_HVAR','INFO', 'FORMAT', 'Sample_Info', 'Ori_REF', 'Ori_ALT', 'OMIM',
       'GWAS_Pubmed_pValue', 'HGMD_ID_Diseasename', 'HGMD_mutation', 'GO_BP',
       'GO_CC', 'GO_MF', 'KEGG_PATHWAY', 'PID_PATHWAY', 'BIOCARTA_PATHWAY',
       'REACTOME_PATHWAY']
group = ['CHROM', 'POS', 'ID', 'REF', 'ALT', 'GeneName',
       'Func', 'Gene', 'GeneDetail', 'ExonicFunc', 'AAChange',
       'cytoBand', 'genomicSuperDups', 'Repeat', 'avsnp150',
       'cosmic70', 'CLNALLELEID', 'CLNDN', 'CLNDISDB', 'CLNREVSTAT', 'CLNSIG',
       'gnomad_exome_AF', 'gnomad_exome_AF_raw', 'gnomad_exome_AF_afr',
       'gnomad_exome_AF_sas', 'gnomad_exome_AF_amr', 'gnomad_exome_AF_eas',
       'gnomad_exome_AF_nfe', 'gnomad_exome_AF_fin', 'gnomad_exome_AF_asj',
       'gnomad_exome_AF_oth', 'SIFT',
       'Polyphen2_HDIV', 'Polyphen2_HVAR', ]
def df_filter(df):
    df = df[keep]
    df = df[df['Func'].isin(['exonic', 'splicing', 'exonic;splicing'])]
    df = df[df['ExonicFunc']!='synonymous SNV']
    df['genomicSuperDups']=='.'
    return df
def flatten_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

cnt = 0
SampleID = samples[0].split('/')[-1].split('.')[0]
df = pd.read_csv(f'result/Mutation/SNP/Annotation/{SampleID}.GATK.snp.annovar.hg38_multianno.xls',sep ='\t')
df = df.rename(columns={SampleID:'Sample_Info'})
df = df_filter(df)
df['SampleID'] = SampleID

for samp in samples[1:]:
    SampleID = samp.split('/')[-1].split('.')[0]
    df1 = pd.read_csv(f'result/Mutation/SNP/Annotation/{SampleID}.GATK.snp.annovar.hg38_multianno.xls',sep ='\t')
    df1 = df1.rename(columns={SampleID:'Sample_Info'})
    df1 = df_filter(df1)
    df1['SampleID'] = SampleID
    combined_df = pd.concat([df, df1])
    df = combined_df.groupby(group, as_index=False).agg({'SampleID': list, 'Sample_Info': list} )
    df['SampleID']= df['SampleID'].apply(flatten_list)
    df['Sample_Info'] = df['Sample_Info'].apply(flatten_list)
    cnt +=1
    print(SampleID, cnt)

df.to_csv('SNP.txt', index = None, sep ='\t')
