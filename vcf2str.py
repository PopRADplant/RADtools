

'''
missing data is 0 not -9
'''
import vcf
from collections import defaultdict
import  numpy  as  np

import optparse


		
class Print_gp(object):
	def __init__(self,vcffile,popmap):
		self.VCF=vcffile
		self.pop=defaultdict()
		self.popmap=popmap
			
	def read_pop(self):
		with open(self.popmap,'r') as POP:
			for line in POP.readlines():
				ind_pop=line.strip().split('\t')
				self.pop[ind_pop[0]]=ind_pop[1]
		return self.pop
				
	def extract_pos(self):
		records=vcf.Reader(open(self.VCF,'r'))
		pos=[]
		for record in records:
			pos.append(str(record.POS))

		return pos	
		
	def vcf2array(self):
		pos=self.extract_pos()
		popdict=self.read_pop()
		n_ind=self.read_pop()
		newarray=np.empty(shape=[2*len(n_ind.keys()),len(pos)+2],dtype=object)
		records=vcf.Reader(open(self.VCF,'r'))
		nuc={'A':'1','C':'2','G':'3','T':'4','-9':'0'}	
		i=0
		for record in records:	
			i+=1	
			n=0
			for sample in record.samples:
				n+=1
				ind=sample.sample
	
				newarray[2*n-1][0]=ind
				newarray[2*n-2][0]=ind
				newarray[2*n-1][1]=popdict[ind]
				newarray[2*n-2][1]=popdict[ind]
				gt=sample.gt_bases
				if gt!=None:
					ref=gt.split('/')[0]
					alt=gt.split('/')[1]
			
				else:
					ref='-9'
					alt='-9'
					gen_gt='0'+nuc[ref]+'0'+nuc[alt]
				newarray[2*n-2][i+1]=nuc[ref]			
				newarray[2*n-1][i+1]=nuc[alt]

		
		return newarray
		

		

				

class WriteStr(object):
		def __init__(self,pos,gparray,out):
			self.strim=open(out,"w")
			self.array=gparray
			self.pos=pos
		
		def write_str(self):
			print "starts vcf2genepop"
			self.strim.write('#this alleles  were showed with  two line one columns\n')#write locus site
			self.strim.write('\t\t'+','.join(self.pos)+'\n')#write locus site
			pop=[]
			for ele in  self.array:
				self.strim.write('\t'.join(ele.tolist())+'\n')
		def close(self):
			print "successful for changing"
			self.strim.close()			
		

if __name__=="__main__": 
	parser = optparse.OptionParser("usage: python %prog -V vcffile -W genepopfile -M popmap")
	parser.add_option("-V", "--input", dest="vcffile",help="the vcffile")
	parser.add_option("-W", "--output", dest="structure",help="the output file name for genepop")
	parser.add_option("-M", "--popdict", dest="popmap",help="the popfile")
	(options, args) = parser.parse_args()
	
	file=options.vcffile
	out=options.structure
	popmap=options.popmap
	
	if file is None:
		print "please input a vcffile"
	elif out is None:
		print "please give a filename for genepop"
	elif popmap is None:
		print "need a popmap file,the format is\
				ind1	pop1	\
				indn	popn	\
				...		....	\
				indx	popx	"
	
	#the next is run vcf2gen
	
	gp2=Print_gp(file,popmap)
	gparray=gp2.vcf2array()
	pos=gp2.extract_pos()
	popdict=gp2.read_pop()
	w2str=WriteStr(pos,gparray,out)
	w2str.write_str()
	w2str.close()
	
