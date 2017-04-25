import gffutils
import pysam

def write_it(name, length, BY, RM):
	outfile.write(name)
        outfile.write("\t")
	outfile.write(str(length))
	outfile.write("\t")
	outfile.write(str(BY))
	outfile.write("\t")
	outfile.write(str(RM))
	outfile.write("\n")

db = gffutils.FeatureDB("yeast.db")
infile_BY = pysam.AlignmentFile("BY_output.sorted.bam", "rb")
infile_RM = pysam.AlignmentFile("RM_output.sorted.bam", "rb")
outfile = open("gene_counts.txt", "w")

outfile.write("mRNA\t")
outfile.write("Gene_length\t")
outfile.write("BY_count\t")
outfile.write("RM_count")
outfile.write("\n")

for mRNA in db.features_of_type('mRNA'):
	if mRNA.chrom == 'chrmt': continue
	count_BY = 0
	count_RM = 0
	length = 0
	name = mRNA["Name"][0]
	for CDS in db.children(mRNA, featuretype = 'CDS'):
		count_BY += infile_BY.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
		count_RM += infile_RM.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
		length += CDS.stop - CDS.start
	write_it(name, length, count_BY, count_RM)

outfile.close()
