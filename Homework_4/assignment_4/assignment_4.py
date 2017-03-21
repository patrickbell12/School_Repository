import pysam
import math
from decimal import Decimal
inputfile = open("chromFa.fasta","r")
outputfile = open("finalFile.txt","w")

def nCr(n,k):
	f = math.factorial
	return f(n) / f(k) / f(n-k)

def gene_probability(n,k):
	epsilon = 0.01
	Reference  = nCr(n,k) * epsilon**k * (1-epsilon)**(n-k)
	Alternative  = nCr(n,k) * (1-epsilon)**k * epsilon**(n-k)
	return Reference, Alternative

def analyze_list(all_reads, ref, n):
	A_count = 0
	C_count = 0
	G_count = 0
	T_count = 0
	ref_count = 0
	for read in all_reads:
		if read.is_del or read.is_refskip: continue
		#get the base at that site in that read and use that instead of all_reads[i]
		base = read.alignment.query_sequence[read.query_position]
		if base == "A":
			A_count += 1
			if base == ref:
				ref_count += 1
		elif base == "C":
			C_count += 1
			if base == ref:
				ref_count += 1
		elif base == "G":
			G_count += 1
			if base == ref:
				ref_count += 1
		elif base == "T":
			T_count += 1
			if base == ref:
				ref_count += 1
	d={'A':A_count,'C':C_count,'G':G_count,'T':T_count}
	biggest = max(d, key=d.get)
	if d[biggest] > ref_count:
		R, A = gene_probability(n, d[biggest])	
		return R, A, biggest
	else: #if ref is equal or more than biggest
		if d[biggest] == ref_count:
			d.pop(biggest, None)
			biggest = max(d, key=d.get)
		R, A = gene_probability(n, d[biggest])
		return R, A, biggest

Genome = []
Genome_Names = inputfile.readline()
Genome_Names = Genome_Names.strip("\n")

mydict = {}
while True:
	line = inputfile.readline()
	if line == "":
		break
	line = line.strip("\n")
	if line[0] == ">":
		mydict[Genome_Names] = ''.join(Genome)
		Genome = []
		Genome_Names = line
		continue
	length = len(line)
	for i in range(length):
		if line[i] == "A":
			Genome.append("A")
		elif line[i] == "C":
			Genome.append("C")
		elif line[i] == "G":
			Genome.append("G")
		elif line[i] == "T":
			Genome.append("T")

mydict[Genome_Names] = str(Genome)
Genome = []
inputfile.close()

for key in mydict.iterkeys():
	print key

outputfile.write("Chromosome\tLocation\tReference\tAlternative\tRprob\t\tAprob\n")

samfile = pysam.AlignmentFile("output.sorted.bam", "rb" )
for pileupcolumn in samfile.pileup():
	n = pileupcolumn.n
	if n<100:
		R, A, alt = analyze_list(pileupcolumn.pileups, mydict[">" + pileupcolumn.reference_name][pileupcolumn.pos], n)			
		if A>R:
			outputfile.write("%s\t\t%s\t\t%s\t\t%s\t\t%.2E\t%.2E\n" %(pileupcolumn.reference_name, pileupcolumn.pos, mydict[">" + pileupcolumn.reference_name][pileupcolumn.pos], alt, Decimal(R), Decimal(A)))

		
samfile.close()
outputfile.close()



