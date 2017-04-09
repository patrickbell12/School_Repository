import pysam

bed_file = open("Intersect_filtered_cov8_chr21_rand1000.bed","r")
while True:
	read = bed_file.readline()
	if read == '':
		break
	read = read.strip('\n')
	read = read.split('\t')
	print read
	raw_input()

bed_file.close()
