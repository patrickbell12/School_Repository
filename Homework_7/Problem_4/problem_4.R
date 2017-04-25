  library("data.table")
  gene_counts = fread("gene_counts.txt",fill=TRUE)
  head(gene_counts)
  #comp_fold = gene_counts[BY_count != 0 & RM_count != 0, .(log_fold = log2(BY_count/RM_count)), by = mRNA]
  #comp_fold
  #pseudo_count = gene_counts[, .(log_fold = log2((BY_count+1)/(RM_count+1))), by = mRNA]
  #pseudo_count
  FPKM = gene_counts[, .(mRNA, FPKM_BY = BY_count/Gene_length*1e9/sum(BY_count), FPKM_RM = RM_count/Gene_length*1e9/sum(RM_count))]
  FPKM

  FPKM_fold = gene_counts[, .(log_fold = log2((BY_count/Gene_length*1e9/sum(BY_count)+1)/(RM_count/Gene_length*1e9/sum(RM_count)+1)))]
  FPKM_fold 