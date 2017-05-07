library('tximport')
library('DESeq2')

#RNA expression section
RNA_files = c('/Users/patrickbell/School_Repository/final_project/files_for_final_project/scer_output_directory_3/abundance.tsv','/Users/patrickbell/School_Repository/final_project/files_for_final_project/scer_output_directory_4/abundance.tsv',
              '/Users/patrickbell/School_Repository/final_project/files_for_final_project/spar_output_directory_3/abundance.tsv','/Users/patrickbell/School_Repository/final_project/files_for_final_project/spar_output_directory_4/abundance.tsv')
names(RNA_files) = c("scer_RNA_1","scer_RNA_2","spar_RNA_1","spar_RNA_2")
txdat_RNA = tximport(RNA_files, type="kallisto", txOut=TRUE)
coldata_RNA = data.frame(condition_RNA=c('S_c_RNA','S_c_RNA','S_p_RNA','S_p_RNA'))
rownames(coldata_RNA)=names(RNA_files)
dds_RNA = DESeqDataSetFromTximport(txdat_RNA, colData= coldata_RNA, design=~ condition_RNA)
dds_RNA = DESeq(dds_RNA)
res_RNA = results(dds_RNA)
res_RNA
sub_table_RNA = subset.data.frame(res_RNA, c(res_RNA$padj)<0.1)
sub_table_RNA #table of differentially expressed genes between the two species at an FDR of 10%
plotMA(sub_table_RNA, main='mRNA expression')



#Ribosome occupancy section
rib_files = c('/Users/patrickbell/School_Repository/final_project/files_for_final_project/scer_output_directory_1/abundance.tsv','/Users/patrickbell/School_Repository/final_project/files_for_final_project/scer_output_directory_2/abundance.tsv',
              '/Users/patrickbell/School_Repository/final_project/files_for_final_project/spar_output_directory_1/abundance.tsv','/Users/patrickbell/School_Repository/final_project/files_for_final_project/spar_output_directory_2/abundance.tsv')
names(rib_files) = c("scer_rib_1","scer_rib_2","spar_rib_1","spar_rib_2")
txdat_rib = tximport(rib_files, type="kallisto", txOut=TRUE)
coldata_rib = data.frame(condition_rib=c('S_c_rib','S_c_rib','S_p_rib','S_p_rib'))
rownames(coldata_rib)=names(rib_files)
dds_rib = DESeqDataSetFromTximport(txdat_rib, colData= coldata_rib, design=~ condition_rib)
dds_rib = DESeq(dds_rib)
res_rib = results(dds_rib)
res_rib
sub_table_rib = subset.data.frame(res_rib, c(res_rib$padj)<0.1)
sub_table_rib #table showing genes with differential ribosome occupancy between the two species at an FDR of 10%
plotMA(sub_table_rib, main='Ribosome occupancy')



#differential translation efficiency section
txdat = tximport(c(RNA_files,rib_files), type = "kallisto", txOut = TRUE)
coldata = data.frame(condition=c('S_c','S_c','S_p','S_p','S_c','S_c','S_p','S_p'),assay=c('RNA','RNA','RNA','RNA','rib','rib','rib','rib'))
rownames(coldata)=names(c(RNA_files,rib_files))
dds = DESeqDataSetFromTximport(txdat, colData = coldata, design= ~ assay + condition + assay:condition)
dds = DESeq(dds, test="LRT", reduced= ~ assay + condition)
res_tran_eff = results(dds)
res_tran_eff

sub_table_tran_eff = subset.data.frame(res_tran_eff, c(res_tran_eff$padj)<0.1)
sub_table_tran_eff #table showing genes with differential translation efficiency between the two species at an FDR of 10% 
plotMA(sub_table_tran_eff, main='Differential Translational Efficiency')


plot(res_RNA$log2FoldChange, res_tran_eff$log2FoldChange, main='RNA abundance vs. Translational efficiency', xlab='Log2 mRNA change', ylab='Log2 translational efficiency change')

up_down = sum(c(res_RNA$padj)<0.1&c(res_RNA$log2FoldChange)>0&c(res_tran_eff$padj)<0.1&c(res_tran_eff$log2FoldChange)<0,na.rm=TRUE) 
  #compensatory evolution RNA up and TE down

down_up = sum(c(res_RNA$padj)<0.1&c(res_RNA$log2FoldChange)<0&c(res_tran_eff$padj)<0.1&c(res_tran_eff$log2FoldChange)>0,na.rm=TRUE)
  #compensatory evolution RNA down and TE up

up_up = sum(c(res_RNA$padj)<0.1&c(res_RNA$log2FoldChange)>0&c(res_tran_eff$padj)<0.1&c(res_tran_eff$log2FoldChange)>0,na.rm=TRUE)
  #coordinated evolution, both UP

down_down = sum(c(res_RNA$padj)<0.1&c(res_RNA$log2FoldChange)<0&c(res_tran_eff$padj)<0.1&c(res_tran_eff$log2FoldChange)<0,na.rm=TRUE)
  #coordinated evolution, both down


a = c("compensatory evolution RNA up and TE down","compensatory evolution RNA down and TE up",
      "coordinated evolution, both up","coordinated evolution, both down")
b = c(up_down,down_up,up_up,down_down)
bubba = data.frame(Gene_Evolution_Condition=a,Count=b)
bubba
