Genome_file = open("my_genome.fa","r")
My_reads = open("my_reads.fastq","r")
match_file = open("Matches_found.txt","w")

chromosome_names = []
genome = []
compGenome = []

def make_dictionary(genome_in, someLength):
	record = []
	my_dict = {}
	temp = []
	genome_length = len(genome_in)	

	print someLength
	print genome_length
	for k in range(genome_length):
		if k<1 and genome_in[k] == "BREAK":
			record.append(k)
			continue
		if genome_in[k+someLength] == "BREAK":
			spot = k+someLength
			record.append(spot)
			k = spot
			if k+1 >= genome_length:
				break
			continue
		
		key = ''.join((genome[k:k+someLength]))
		my_dict[key]=k
	return my_dict, record

def run_through_genome(read, dictionary_in, record, name, P_or_M):	
	if P_or_M == True:
		sense = "+"
	else:
		sense = "-"

	read_length = len(read)
	for key in dictionary_in.iterkeys():
		#print len(list(key))
		#match_file.write(key)
		if read == key:
			print "match found"
			big_number = dictionary_in[key]
			for i in range(len(record)):
				if big_number<record[i] == True:
					place = big_number - record[(i-1)]
					break
			match_file.write("Read %s found a match on the %c chromosome number %d at position %d\n" %(str(name), sense, (i-1), place))
			return
	return None

while True:
	line = Genome_file.readline()
	if line =="":
		break	
	line_list = list(line)
	if line_list[0] == '>':
		chromosome_names.append(line)
		genome.append("BREAK")
		compGenome.append("BREAK")
		print "THis happend"
		continue
	for i in range(len(line_list)):
		if line_list[i] == "A":
			compGenome.append("T")
			genome.append("A")
		elif line_list[i] == "C":
			compGenome.append("G")
			genome.append("C")
		elif line_list[i] == "G":
			compGenome.append("C")
			genome.append("G")
		elif line_list[i] == "T":
			compGenome.append("A")
			genome.append("T")
compGenome.append("BREAK")
genome.append("BREAK")

k=0
constant = 0
while True:
	name = My_reads.readline()
	if name == "":
		break
	seq = My_reads.readline()
	name2 = My_reads.readline()
	qual = My_reads.readline()
	k+=1
	if constant == 0:
		positive_dict, positive_record = make_dictionary(genome, len(list(seq)))
		negative_dict, negative_record = make_dictionary(compGenome, len(list(seq)))
		print "finished making dictionaries"
		constant = 1
	
	if k%200 == 0:
		print k


	run_through_genome(seq, positive_dict, positive_record, name, True)
	run_through_genome(seq, negative_dict, negative_record, name, False)

print k

Genome_file.close()
My_reads.close()
match_file.close()


