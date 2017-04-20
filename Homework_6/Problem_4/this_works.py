import gffutils
import pysam
import numpy as np
import scipy.stats as st

db = gffutils.FeatureDB("yeast.db")
infile_BY = pysam.AlignmentFile("BY_output.sorted.bam", "rb")
infile_RM = pysam.AlignmentFile("RM_output.sorted.bam", "rb")
outfile = open("diff_expression.txt", "w")

outfile.write("mRNA\t")
outfile.write("BY count\t")
outfile.write("RM count\t")
outfile.write("p value\t")
outfile.write("\n")

total_reads_BY = 0
total_reads_RM = 0

def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)

def get_LRT_and_p(count_BY, count_RM):
	lambda1 = (float(count_BY)/total_reads_BY+float(count_RM)/total_reads_RM)/2
	lambda11 = float(count_BY)/total_reads_BY
	lambda21 = float(count_RM)/total_reads_RM
	prob_data_null = st.poisson.pmf(count_BY, total_reads_BY*lambda1)*st.poisson.pmf(count_RM, total_reads_RM*lambda1)
	prob_data_alt = st.poisson.pmf(count_BY, total_reads_BY*lambda11)*st.poisson.pmf(count_RM, total_reads_RM*lambda21)
	LRT = 2*(np.log(prob_data_alt) - np.log(prob_data_null))
	p_value = st.chi2.sf(LRT,df=1)

	return LRT, p_value


#Get total reads of each alignment file
for mRNA in db.features_of_type('mRNA'):
	for CDS in db.children(mRNA, featuretype = 'CDS'):
		if CDS.chrom != 'chrmt':
			name = CDS["Name"][0]
			total_reads_BY += infile_BY.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
			

for mRNA in db.features_of_type('mRNA'):
	for CDS in db.children(mRNA, featuretype = 'CDS'):
		if CDS.chrom != 'chrmt':
			name = CDS["Name"][0]
			total_reads_RM += infile_RM.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
			

for mRNA in db.features_of_type('mRNA'):
	for CDS in db.children(mRNA, featuretype = 'CDS'):
		if CDS.chrom != 'chrmt':
			name = CDS["Name"][0]
			count_BY = infile_BY.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
			count_RM = infile_RM.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
			
			#raw_input()
			if (hasNumbers(str(count_BY)) and hasNumbers(str(count_RM)) == True) and (count_BY and count_RM != 0):
				LRT, p_value = get_LRT_and_p(count_BY,count_RM)
				if p_value < 0.05:
					outfile.write(name)
					outfile.write("\t")
					outfile.write(str(count_BY))
					outfile.write("\t")
					outfile.write(str(count_RM))
					outfile.write("\t")
					outfile.write(str(p_value))
					outfile.write("\n")

outfile.close()
