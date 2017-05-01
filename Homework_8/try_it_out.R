library('tximport')
library('DESeq2')

 files = c("/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_1/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_2/abundance.tsv",
            "/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_3/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_4/abundance.tsv",
            "/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_5/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_6/abundance.tsv",
            "/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_7/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_8/abundance.tsv",
            "/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_9/abundance.tsv","/Users/patrickbell/School_Repository/Homework_8/problem_1/output_directory_10/abundance.tsv")
  names(files) = c("sample1","sample2","sample3","sample4","sample5","sample6","sample7","sample8","sample9","sample10")
  txdat = tximport(files, type="kallisto", txOut=TRUE)
  coldata = data.frame(condition=c('SNF2','SNF2','SNF2','SNF2','SNF2','WT','WT','WT','WT','WT'))
  rownames(coldata)=names(files)
  dds = DESeqDataSetFromTximport(txdat, colData= coldata, design=~ condition)
  dds = DESeq(dds)
  res = results(dds)
  res
  plotMA(res)
  dds <- estimateSizeFactors(dds)
  dds <- estimateDispersions(dds)
  plotDispEsts(dds)
  #these tell me that, for each gene, the more times it is counted, the lower its dispersion is from its biological expression level.
  
  sum(c(res$padj)<0.05,na.rm=TRUE) #this was second try
  sum(c(res$pvalue)<0.05,na.rm=TRUE) 
  
#  a = (1:length(res_false_discovery)) #this was first try
#  NFD = 0
#  RPV = 0
#  for (i in a){
#    b = res$padj[i]
#    c = res$pvalue[i]
#    if (!is.na(b)){
#      if ((b<0.05)){NFD = NFD + 1}
#    }
#    if (!is.na(c)){
#      if ((c<0.05)){RPV = RPV + 1}
#    }
# }
#  NFD
#  RPV