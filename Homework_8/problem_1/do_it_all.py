import os

samples = ['SNF2_1','SNF2_2','SNF2_3','SNF2_4','SNF2_5','WT_1','WT_2','WT_3','WT_4','WT_5']
i=0
for sample in samples:
	i += 1
	command = 'kallisto quant -i transcripts.idx -o output_directory_%d --single -l 180 -s 20 %s.fastq.gz'%(i, sample)
	print "Currently running: %s"%command
	os.system(command)
