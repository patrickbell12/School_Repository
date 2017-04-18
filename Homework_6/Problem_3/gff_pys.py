import pysam
import gffutils
db = gffutils.FeatureDB("yeast.db")
infile = pysam.AlignmentFile("output.sorted.bam", "rb")
outfile = open("gene_FPKM.txt", "w")

mydict = {}
total = 0

for mRNA in db.features_of_type('mRNA'):
	for CDS in db.children(mRNA, featuretype = 'CDS'):
		if CDS.chrom != 'chrmt':
			name = CDS["Name"][0]
			count = infile.count(reference = CDS.chrom, start=CDS.start,end=CDS.stop)
			if CDS.stop-CDS.start != 0:
				count = float(count)/(CDS.stop-CDS.start)*1000000000
				mydict[name] = count
				total += count

for key, value in sorted(mydict.items()):
	FPKM = str(value/total)
	outfile.write(key)
	outfile.write("\t")
	outfile.write(FPKM)
	outfile.write("\n")
	



