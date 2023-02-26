#Pipeline to create a single annotated Excel file from all VCF files
#The first several steps are to handle files that were created with Novogene
#In which the SNP and INDEL files from same patient are split up 


#I need to add sbatch dependencies - otherwise this wont work at all 
job_ids=()

#For WES samples
#Filter vcf files to exome only 
#Assumed multiple directories of SNP files labeled *_SNP
for dir in *_SNP; 
   do
   for file in $dir/*.gz;
   do         
      filename=$(basename $file);         
      job_id=$(sbatch -t 0:10:00 --wrap="ml bcftools;bcftools view -R /scratch4/wisaacs1/hg19_Exome_splice.bed  $file -O z -o /scratch4/wisaacs1/FILT-SNP/$filename" | awk '{print $4}')
      job_ids+=($job_id)
   done
done


#same for indels 
for dir in *_INDEL; 
   do
   for file in $dir/*.gz;
   do         
      filename=$(basename $file);         
      job_id=$(sbatch -t 0:10:00 --wrap="ml bcftools;bcftools view -R /scratch4/wisaacs1/hg19_Exome_splice.bed  $file -O z -o /scratch4/wisaacs1/FILT-INDEL/$filename"| awk '{print $4}') 
      job_ids+=($job_id)
   done 
done

#Now concatenate the SNP and INDEL files from the same individual
#Dependent on the previous jobs finishing 
#It is probably better to switch the code around so that each sample recieves a single job where SNP, INDEL and Concat are all performed together 
IFS=":"
sbatch -J Concatenate --dependency=afterok:"${job_ids[*]}" --wrap="for file in *.indel.vcf.gz; do    ;   sampleID=$(basename "$file" | cut -d '.' -f 1);    ;   bcftools concat -a $sampleID.GATK.indel.vcf.gz /scratch4/wisaacs1/FILT-SNP/$sampleID.GATK.snp.vcf.gz -O z -o /scratch4/wisaacs1/Concat/$sampleID.vcf.gz; done" 

# List of all samples
ls Concat/*gz > samples.txt

#Merge all samples 
sbatch -J Merge -t 24:00:00 -N 4 -n 24 -o Merge.out -e Merge.err --wrap="ml bcftools; bcftools merge -m none --threads 96 -l samples.txt -O z -o Merge.vcf.gz”

#Normalize to remove multi-allelic line in the VCF file `
sbatch -t 1:00:00 -N 1 -n 24 -e index.err -o index.out --wrap="ml bcftools; bcftools norm -m - Merge.vcf.gz -O z -o merge.norm.vcf.gz --threads 24”

#Annotate with Annovar 
#Include REfgene, Supdups, gnomad, clinvar, cosmic
perl /scratch4/jluo2/drabiza1/Annovar/table_annovar.pl  /scratch4/wisaacs1/Expansion2/merge.norm.vcf.gz  humandb/ -buildver hg19 -out /scratch4/wisaacs1/Expansion2/myanno -remove -protocol refGene,avsnp150,genomicSuperDups,gnomad211_exome,clinvar_20220320,cosmic95,ljb23_sift -operation g,f,r,f,f,f,f -nastring . -vcfinput -polish --thread 96

sed 's/\.\/\.:\.:\.:\.:\./\./g' myanno.hg19_multianno.txt > edit_myanno.hg19_multianno.txt.vcf


