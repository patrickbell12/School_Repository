import gffutils
db = gffutils.FeatureDB("yeast.db")

out_file = open("outfile.txt","w")

hold = ''
out_file.write("CDS colomn")
out_file.write("\t")
out_file.write("Length colomn")
out_file.write("\n")

for mRNA in db.features_of_type('mRNA'):
       for CDS in db.children(mRNA, featuretype = 'CDS'):
	       temp = CDS["Name"][0]
	       if temp != hold:
		       out_file.write(temp)
		       out_file.write("\t")
		       length = CDS.stop - CDS.start
		       out_file.write(str(length))
		       out_file.write("\n")
		       hold = temp
#	       raw_input()
out_file.close()
