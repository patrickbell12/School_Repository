import collections
my_genome = open("my_genome.fa","r")
my_reads = open("my_reads.fastq","r")

genome = []
compGenome = []
ChromosomeNumber = 0

def rotate(something):
	item = collections.deque(something)
	item.rotate(-1)
	return list(collections.deque(item))

def BWT(L):
	arrays = []
	first_list = []
	last_list = []
	# L is a list of nucleotides
	len_L = len(L)
	print len_L
	L.append("$")
	# Build suffix arrays
	arrays.append(L)
	for i in range(len_L):
		L = rotate(L)
		thingy = str(L)
		arrays.append(thingy)
		if i%100==0:
			print i
		
		# At end, you have list of all suffixes as a List (LIST IN LIST)
	#Organize Lexicographicaly
	print "About to sort arrays"
	arrays.sort()
	print "Arrays sorted"

	#Make lists of first and Last collumn 
	last_spot = len(arrays)
	for i in range(last_spot):
		first_list.append(arrays[i][0])
		last_list.append(arrays[i][last_spot-1])

#	for i in range(len(arrays)):
#		print arrays[i]
#	print first_list
#	print last_list

	return last_list

#in_string = "CCTGAGAATCGGT"
#list_L = list(in_string)

#BWT(list_L)
constant = 0
while True:
	line = my_genome.readline()
	if line =="":
		break
	line = line.strip()
	line_list = list(line)
	if line_list[0] == '>':
		if constant == 1:
			break
		if constant == 0:
			chromosome_name = line
			constant += 1
			ChromosomeNumber += 1
			continue
		#write old chromosome into its file
		
#		with open("Chrom_file_" + chromosome_name + ".txt","w") as f:
#			S_BWT = BWT(genome)
#			AS_BWT = BWT(compGenome)
#			f.write("This is the sense strand >>>>>  ", S_BWT)
#			f.write("This is the anti-sense strand >>>>>  ", AS_BWT)
		#initiate new chromosome read
#		chromosome_name = line
#		continue


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

print "GOT HERE"

with open("Chrom_file_" + str(ChromosomeNumber) + ".txt","w") as f:
	S_BWT = BWT(genome)
	#AS_BWT = BWT(compGenome)
	f.write("This is the sense strand >>>>>   ", str(S_BWT))
	#f.write("This is the anti-sense strand >>>>>   ", str(AS_BWT))


# FOR WHEN READS ARE NEEDED
#while True:
#	name = my_reads.readline()
#	if name == "":
#		break
#	seq = my_reads.readline()
#	name2 = my_reads.readline()
#	qual = my_reads.readline()






