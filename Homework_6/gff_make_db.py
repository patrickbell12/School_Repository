import gffutils

check_file = open("check_file.txt","r+")

variable = check_file.read(1)

if variable != "1":
	db = gffutils.create_db("saccharomyces_cerevisiae.gff",dbfn="yeast.db",merge_strategy="merge",force=True,verbose=True)
	print "The database has been made"
	check_file.write("1")
check_file.close()

if variable == "1":
	print "Function has already been performed. It is not recomended to perfrom a second time"

