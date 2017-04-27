  files = c("/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_1/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_2/abundance.tsv",
            "/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_3/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_4/abundance.tsv",
            "/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_5/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_6/abundance.tsv",
            "/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_7/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_8/abundance.tsv",
            "/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_9/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_10/abundance.tsv")
  names(files) = c("sample1","sample2","sample3","sample4","sample5","sample6","sample7","sample8","sample9","sample10")
  txdat = tximports(files, type="kallisto", txOut=TRUE)