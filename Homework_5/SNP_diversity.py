import pysam
import itertools
import random

vcf_in = pysam.VariantFile("greatapes.fixedchr21.vcf.gz")
vcf_out = pysam.VariantFile('-', 'w', header=vcf_in.header)
#out_file = open("thoihoshgt.txt","w")
tbx = pysam.TabixFile("greatapes.fixedchr21.vcf.gz")

sample_list = list((vcf_in.header.samples))

def analyse_allele_site(list_in):	
	allele = []
	pi = 0
	for i in range(len(list_in)):
		temp = list_in[i]
		temp = list(temp)
		if temp[0] != temp[2] and temp[0] != '.':
			this = bool(random.getrandbits(1))
			if this == True:
				allele.append(1)
			elif this == False:
				allele.append(0)
		if temp[0] == temp[2] and temp[0] != '.':
			this = temp[0]
			if this == '1':
				allele.append(1)
			elif this == '0':
				allele.append(0)

	for pair in itertools.combinations(allele, r=2):
		temp = list(pair)
		if temp[0] != temp[1]:
			pi += 1
	return float(pi)/10


def deal_with_samples():
	#specify desired genea, CAPITALIZE! 
	sample1 = 'Homo'	#name of 1
	sample1_locations = []
	sample2 = 'Pan'		#name of 2
	sample2_locations = []
	
	#enter test size
	test_size = 5

	#chop off ends (who cares, right)
	new_list = [i.split('_', 1)[0] for i in sample_list]

	#collect samples
	J=0
	K=0
	for i in range(len(new_list)):
		name = new_list[i]
		if name == sample1:
			J+=1
			if J > test_size:
				continue
			sample1_locations.append(i)
		if name == sample2:
			K+=1
			if K > test_size:
				continue
			sample2_locations.append(i)

	#now you know what coloms have each genea
	return sample1, sample1_locations, sample2, sample2_locations

#collect test subjects

subject1_name, subject1, subject2_name, subject2 = deal_with_samples()

#collect SNP locations
bed_file = open("Intersect_filtered_cov8_chr21_rand1000.bed","r")
SNP_list = []
S1 = 0
S2 = 0
Pi1 = 0
Pi2 = 0
while True:
	read = bed_file.readline()
	if read == '':
		break
#	format read into: str, int, int
	read = read.strip('\n')
	read = read.split('\t')
	name = read[0]
	start = int(read[1])
	stop = int(read[2])
	

	for row in tbx.fetch(name, start, stop, parser=pysam.asTuple()):
		list1 = []
		list2 = []
		ref = row[3]
		alt = row[4]

		for i in range(len(subject1)):
			list1.append(row[subject1[i]])
#		print ("from species 1 ----->", list1)
		for i in range(len(subject2)):
			list2.append(row[subject2[i]])
#		print ("from species 2 ----->", list2)
		list1 = [i.split(':', 1)[0] for i in list1]
		temp = list1[0]
		temp = list(temp)
		if temp[0] != '.':
			Pi1 += analyse_allele_site(list1)
			S1 += 5		
		
		list2 = [i.split(':', 1)[0] for i in list2]
		temp = list2[0]
		temp = list(temp)
		if temp[0] != '.':
			Pi2 += analyse_allele_site(list2)
			S2 += 5 
		
	

bed_file.close()

print "Genus", subject1_name,"has Pi diversity of", Pi1,"and S value of", S1
print "Genus", subject2_name,"has Pi diversity of", Pi2,"and S value of", S2

if Pi1 > Pi2:
	print subject1_name,"has more diversity than", subject2_name
if Pi2 > Pi1:
	print subject1_name,"has more diversity than", subject2_name





