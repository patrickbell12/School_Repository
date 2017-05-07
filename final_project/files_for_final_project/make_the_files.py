import os

scer_samples = ['Scer_ribo_seq_1','Scer_ribo_seq_2','Scer_RNA_seq_1','Scer_RNA_seq_2']

spar_samples = ['Spar_ribo_seq_1','Spar_ribo_seq_2','Spar_RNA_seq_1','Spar_RNA_seq_2']

i=0
for sample in scer_samples:
	i += 1
	command = 'kallisto quant -i S_c_transcripts.idx -o scer_output_directory_%d --single -l 180 -s 20 %s.fastq.gz'%(i, sample)
	print "Currently running: %s"%command
	os.system(command)

i=0
for sample in spar_samples:
	i += 1
	command = 'kallisto quant -i S_p_transcripts.idx -o spar_output_directory_%d --single -l 180 -s 20 %s.fastq.gz'%(i, sample)
	print "Currently running: %s"%command
	os.system(command)                                
