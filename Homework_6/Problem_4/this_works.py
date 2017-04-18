import gffutils
import pysam
import numpy as np
import scipy.stats as st

db = gffutils.FeatureDB("yeast.db")
infile_BY = pysam.AlignmentFile("BY_output.sorted.bam", "rb")
infile_RM = pysam.AlignmentFile("RM_output.sorted.bam", "rb")
outfile = open("gene_FPKM.txt", "w")

total_reads_BY = 0
total_reads_RM = 0

#Get total reads of each alignment file
for mRNA in db.features_of_type('mRNA'):
	for CDS in db.children(mRNA, featuretype = 'CDS'):
		if CDS.chrom != 'chrmt':
			name = CDS["Name"][0]
			count = infile_BY.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
			total_reads_BY += count 

for mRNA in db.features_of_type('mRNA'):
	for CDS in db.children(mRNA, featuretype = 'CDS'):
		if CDS.chrom != 'chrmt':
			name = CDS["Name"][0]
			count = infile_RM.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
			total_reads_RM += count

for mRNA in db.features_of_type('mRNA'):
	for CDS in db.children(mRNA, featuretype = 'CDS'):
		if CDS.chrom != 'chrmt':
			name = CDS["Name"][0]
			count_BY = infile_BY.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
			count_RM = infile_RM.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
			
			lambda1 = (float(count_BY)/total_reads_BY+float(count_RM)/total_reads_RM)/2
			lambda11 = float(count_BY)/total_reads_BY
			lambda21 = float(count_RM)/total_reads_RM
			
			prob_data_null = st.poisson.pmf(count_BY, total_reads_BY*lambda1)*st.poisson.pmf(count_RM, total_reads_RM*lambda1)
			prob_data_alt = st.poisson.pmf(count_BY, total_reads_BY*lambda11)*st.poisson.pmf(count_RM, total_reads_RM*lambda21)
			LRT = 2*(np.log(prob_data_alt) - np.log(prob_data_null))
			p_value = st.chi2.sf(LRT,df=1):





