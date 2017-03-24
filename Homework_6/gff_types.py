import gffutils
db = gffutils.FeatureDB("yeast_database.db")

out_file = open("outfile.txt","w")

for type in db.featuretypes():
	out_file.write(type)
	out_file.write("\n")
	hold = ''
	this = type
	
	for feature in db.features_of_type(this):
	#               if parent.featuretype:
		comp = feature.featuretype
		if comp != hold:
			out_file.write("\t")
			out_file.write(feature.featuretype)
			out_file.write("\n")
			hold = comp
