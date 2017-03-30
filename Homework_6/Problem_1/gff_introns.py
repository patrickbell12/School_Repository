import gffutils
db = gffutils.FeatureDB("yeast.db")

intron_number = 0
gene_number = 0



for mRNA in db.features_of_type('mRNA'):
	gene_number += 1
#	for parent in db.parents(mRNA):
#		print parent
#		if parent == "gene":
#			print "parent is gene"
#		for gene in db.children(parent, featuretype = 'gene'):
#			gene_number += 1
#			print gene, "Gene parent -> ", parent

for intron in db.features_of_type('intron'):
	intron_number += 1
	for parent in db.parents(intron):
		varb = parent.featuretype
		if varb == 'mRNA':	
			name = parent["Name"][0]
			print name, 'is and intron sequence'


fraction = float(intron_number) / float(gene_number)
print "The fraction of introns to genes is---> ", fraction

