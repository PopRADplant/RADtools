#this script was used to change vcf file to arliquin prepare for anlayse of molecular variance.
#this scripts we are assumed you have a pdgspide.jar
#prepare three file:spid file and popopulation definiation file

the examples for population definiation file:
"""
# spid-file generated: Fri Mar 17 16:21:56 CST 2017
# VCF Parser questions
PARSER_FORMAT=VCF
# Only output SNPs with a phred-scaled quality of at least:
VCF_PARSER_QUAL_QUESTION=
# Select population definition file:
VCF_PARSER_POP_FILE_QUESTION=
# What is the ploidy of the data?
VCF_PARSER_PLOIDY_QUESTION=DIPLOID
# Do you want to include a file with population definitions?
VCF_PARSER_POP_QUESTION=true
# Output genotypes as missing if the phred-scale genotype quality is below:
VCF_PARSER_GTQUAL_QUESTION=
# Do you want to include non-polymorphic SNPs?
VCF_PARSER_MONOMORPHIC_QUESTION=false
# Only output following individuals (ind1, ind2, ind4, ...):
VCF_PARSER_IND_QUESTION=
# Only input following regions (refSeqName:start:end, multiple regions: whitespace separated):
VCF_PARSER_REGION_QUESTION=
# Output genotypes as missing if the read depth of a position for the sample is below:
VCF_PARSER_READ_QUESTION=
# Take most likely genotype if "PL" or "GL" is given in the genotype field?
VCF_PARSER_PL_QUESTION=false
# Do you want to exclude loci with only missing data?
VCF_PARSER_EXC_MISSING_LOCI_QUESTION=false

# Arlequin Writer questions
WRITER_FORMAT=ARLEQUIN

# Specify which data type should be included in the Arlequin file  (Arlequin can only analyze one data type per file):
ARLEQUIN_WRITER_DATA_TYPE_QUESTION=SNP
# Specify the DNA locus you want to write to the Arlequin file or write "CONCAT" for concatenation:
ARLEQUIN_WRITER_ONCATENATE_QUESTION=
# Specify the locus/locus combination you want to write to the Arlequin file:
ARLEQUIN_WRITER_LOCUS_COMBINATION_QUESTION=
"""
import glob
import os
import parse

parse=opt.argument("this is the tools vcf to arlequin")
parse=("vcffile",-dest="inputfile",format="vcf")

for file1 in glob.glob("*_sorted.vcf"):
	file2=file1.split('_sorted.vcf')[0]
	format1="VCF"
	format2="ARLEQUIN"
	file3="vcf2alr.spid"
	popmap=/lustre/home/xiaojianhua/data/plink_4/32_matrix_bayes/popmap.txt
	os.system('java -Xmx1024m -Xms512m -jar /lustre/home/xiaojianhua/PGDSpider_2.0.9.0/PGDSpider2-cli.jar -inputfile  %s  -inputformat %s -outputfile %s -outformat %s -spid %s')%(file1,format1,file2,format2,file3)


