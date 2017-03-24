#loop over changable feature
import gffutils

db = gffutils.FeatureDB("yeast_database.db")

for mRNA in db.features_of_type("mRNA"):
	for CDS in db.children(mRNA,featuretype="CDS"):
		print CDS.start, CDS.stop


#for mRNA in db.features_of_type("mRNA"): print mRNA["Name"], mRNA.start, mRNA.stop
