My_reads = open("my_reads.fastq","r")
Genome_File = open("my_genome.fa","r")
matchFile = open("Matches.txt","w")

def compute_match(line1, line2):
	length = len(line1)
	if length != len(line2):
		return None
		print "Did not line up"
	spot = 0
	for i in range(length):
		if line1[i] == line2[i]:
			spot += 1
	return float(spot)/float(length)

def match_read_to_line(genome, sequence, sequence_name, P_or_M):
	chromosome_number = 1
	count = 0
	if P_or_M == True:
		side = "+"
	else:
		side = "-"
	
	gen_len = len(genome)
	seq_len = len(sequence)
	last_point = gen_len-seq_len
	for i in range(last_point):
		count +=1
		if genome[i] == "BREAK":
			i += 1
			chromosome_number += 1
			count = 0
		if sequence[0] == genome[i]:
			temp = []
			for k in range(seq_len):
				x = k + i
				temp.append(genome[x])
			match = compute_match(sequence, temp)
			if match == 1.:
				matchFile.write("--> %s has a match at position %d on the %d %c chromosome\n"%(sequence_name, count, chromosome_number, side))
				break
		if i == last_point:
			return None
			
			
def get_chromosome():
	#Read Genome file into list
	Genome_Names = []
	Genome = []
	compGenome = []
	Genome_Names.append(Genome_File.readline())
	while True:
		line = Genome_File.readline()
		if line == "":
			break
		line_list = list(line)
		if line_list[0] == ">":
			Genome_Names.append(line)
			Genome.append("BREAK")
			compGenome.append("BREAK")
			continue
		length = len(line_list)
		#BUILD CHROMOSOME BY LINE
		for i in range(length):
			if line_list[i] == "A":
				compGenome.append("T")
				Genome.append("A")
			elif line_list[i] == "C":
				compGenome.append("G")
				Genome.append("C")
			elif line_list[i] == "G":
				compGenome.append("C")
				Genome.append("G")
			elif line_list[i] == "T":
				compGenome.append("A")
				Genome.append("T")
#			else:
#				print("That went wrong, better stop this thing")
#				print line[i]
	return Genome_Names, Genome, compGenome

Name_list, plusStrand, minusStrand = get_chromosome()


this = 0
while True:
	name = My_reads.readline()
	if name == "":
		break
	seq = My_reads.readline()
	name2 = My_reads.readline()
	qual = My_reads.readline()
	
	match_read_to_line(plusStrand, seq, name, True)
	match_read_to_line(minusStrand, seq, name, False)
	this+=1
	if this%1000 == 0:
		print this








matchFile.close()
My_reads.close()
Genome.close()
outFile.close()

