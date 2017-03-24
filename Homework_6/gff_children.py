import gffutils
out_file = open("outfile.txt","w")
db = gffutils.FeatureDB("yeast_database.db")



for intron in db.features_of_type("intron"):
	for parent in db.parents(intron):
#		if parent.featuretype:
		out_file.write(parent.featuretype)
		out_file.write("\t")
		out_file.write(intron.name)
		out_file.write("\n")
