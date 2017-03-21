# THis is a combination of assignments 2 and 3
import pysam
import matplotlib.pyplot as plt
infile = pysam.AlignmentFile("output.sorted.bam", "rb")
outfile = pysam.AlignmentFile("test.txt", "w", template=infile)

constant = 0
big_list = []

for read in infile.fetch():
	big_list.append(read.mapping_quality)
	
#	if constant == 20:
#		break
#	constant += 1

plot= plt.hist(big_list,bins=50)
plt.title("Histogram of mapping quality")
plt.xlabel("Mapping Quality")
plt.ylabel("Frequency")
plt.savefig("Mapping_Histogram.jpg")
plt.show(plot)
plt.clf()

true=0
false=0

for read in infile.fetch():
	variable = read.is_reverse
	if variable == True:
		true+=1
	if variable == False:
		false+=1

total = true + false

true_ratio = float(true)/total 
false_ratio = float(false)/total

print "The ratio of reads on the + strand is ", false_ratio
print "The ratio of reads on the - strand is ", true_ratio


