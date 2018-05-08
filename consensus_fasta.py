#! /usr/bin/env python

import re, sys, os, itertools, sets, getopt        # Load standard modules I often use
import gzip


"""
This script will take in a vcf file output from stacks, take the set of loci present in the vcf file, query the stacks database for the consensus sequence, and output a fasta file.
"""
def main(argv):
	try:
		opts,args = getopt.getopt(argv,'h:o:s:m:',)
	except getopt.GetOptError:
		print "ConsensusFasta.py -s <path to Stacks catalog tags name> -m <path to input plinkmap> -o <path to output directory and filename (default ./plink.fasta)> "
		sys.exit(2)
			

	stackscat = ''
	output = './plink.fasta'
	plinkmap = ''

	for opt, arg in opts:

		if opt == "-h":
			print "consensusFasta.py -s <path to input vcf file> -o <path to output directory and filename (default ./vcf.fasta)> "
			sys.exit(2)
		elif opt == "-o":
			output = arg
		elif opt == "-s":
			stackscat = arg
			print stackscat
		elif opt == "-m":
			plinkmap= arg


	pmap = open(plinkmap,"r")

	#Get list of loci from vcf file
	lociused = []
	
	
	for line in pmap:
		if line[0] != "#":
			newline = re.split("\t|_",line)
			if newline[1] not in lociused:
				lociused.append(newline[1])
			else:
				pass
		else:
			pass


	
	dictAA={}
	
	for line in gzip.GzipFile(stackscat,'r'):
		if line[0]!="#":
			newline=line.split("\t")
			dictAA[newline[2]]=newline[9]
	
	seqs = []		
	for locus in lociused:
		seqs.append(dictAA[locus])



	#For each locus, create a list of all consensus sequences in the order of the locus list.


	print "%d loci in the catalog"%len(lociused)


	fastaout = open(output,"w")

	#Write new fasta file.
	for i in range(0,len(lociused)):	
		fastaout.write(">%s\n%s\n"%(lociused[i],seqs[i]))

	pmap.close()
	fastaout.close()


if __name__ == "__main__":
		main(sys.argv[1:])
