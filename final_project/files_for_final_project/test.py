import roman

Cerevisiae_genome = open('S_cerevisiae.fa','r')
C_bed = open('S_cerevisiae_genes.bed','r')
Paradoxus_genome = open('S_paradoxus.fa','r')
P_bed = open('S_paradoxus_genes.bed','r')

C_out = open('S_cerevisiae_proteome.fasta','w')
P_out = open('S_paradoxus_proteome.fasta','w')

C_dict = {}
P_dict = {}

alt_map = {'ins':'0'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

def reverse_complement(seq):
	for k,v in alt_map.iteritems():
		seq = seq.replace(k,v)
	bases = list(seq) 
	bases = reversed([complement.get(base,base) for base in bases])
	bases = ''.join(bases)
	for k,v in alt_map.iteritems():
		bases = bases.replace(v,k)
	return bases

def get_number(header):
	header = header.strip('\n')
	header = header.split(' ')
	chrom_n = header[0]
	chrom_n = chrom_n.split('_')
	number = chrom_n[1]
	return int(number)

def get_roman(chrom):
	chrom = list(chrom)
	n = len(chrom)
	num = chrom[3:n]
	num = ''.join(num)
	num=roman.fromRoman(num)
	return num

while True:
	header = Cerevisiae_genome.readline()
        if header =='':
		break
	chrom = Cerevisiae_genome.readline()
	chrom = chrom.strip('\n')
	chrom_num = get_number(header)

	C_dict[str(chrom_num)] = chrom

while True:
	line = C_bed.readline()
	if line == '':
		break
	line = line.strip('\n')
	line = line.split('\t')		
	bed_chrom = line[0]
	bed_chrom_num = get_roman(bed_chrom)

	start = int(line[1])
	stop = int(line[2])
	gene = line[3]
	sense = line[5]

	sequence = C_dict[str(bed_chrom_num)]
	sequence_list = list(sequence)
	transcript = ''.join(sequence_list[(start-1):(stop-1)])

#	if gene == 'YDR395W':
#		print bed_chrom_num
#		print gene
#		print transcript
#		print len(sequence)
#		raw_input()

	if sense == '-':
		transcript = reverse_complement(transcript)
		C_out.write('>')
		C_out.write(gene)
		C_out.write('\n')
		C_out.write(transcript)
		C_out.write('\n')
	else:
		C_out.write('>')
		C_out.write(gene)
		C_out.write('\n')
		C_out.write(transcript)
		C_out.write('\n')
			
#now do for other one

while True:
	header = Paradoxus_genome.readline()
	if header =='':
		break
	chrom = Paradoxus_genome.readline()
	chrom = chrom.strip('\n')
	chrom_num = get_number(header)

	P_dict[str(chrom_num)] = chrom
	

while True:
	line = P_bed.readline()
	if line == '':
		break
	line = line.strip('\n')
	line = line.split('\t')         
	bed_chrom = line[0]
	bed_chrom_num = get_number(bed_chrom) #chromosome number from bed file
	
	start = int(line[1]) #Start position
	stop = int(line[2]) #End position
	gene = line[3] #gene name
	gene = gene.split('.')[0]
	sense = line[5] #positive or negative 

	sequence = P_dict[str(bed_chrom_num)]

	sequence_list = list(sequence)
	transcript = ''.join(sequence_list[(start-1):(stop-1)])
	if sense == '-':
		transcript = reverse_complement(transcript)
		P_out.write('>')
		P_out.write(gene)
		P_out.write('\n')
		P_out.write(transcript)
		P_out.write('\n')
	else:
		P_out.write('>')
		P_out.write(gene)
		P_out.write('\n')
		P_out.write(transcript)
		P_out.write('\n')



Cerevisiae_genome.close()
C_bed.close()
Paradoxus_genome.close()
P_bed.close()
C_out.close()
P_out.close()

