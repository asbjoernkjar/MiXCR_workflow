# MiXCR_workflow
workflow for running MiXCR on HPC cluster 


Settings are optimized for AmpliSeq for Illumina TCR beta-SR Panel kit - using DNA material
Exctracts only TCR-beta clones --> others are false positives 


generates "final_MiCXR_report.tsv" at path "report path"
summarises stats from the run
- Total_reads: total reads in samples
- Aligned_reads: # reads aligned (to any TCR/BCR chain, but 99.99% align to TCR-B)
- Fraction_overlapped: fraction of reads that overlap (not neccesarily aligned),
     all succesfull TCR-B reads should overlap. non-overlapping are low quality reads
- N_clones: # of unique TCR-beta clone extracted
- Used_reads: # reads used in the final clone count
- PCR_correct_dropped_reads: # of reads dropped during PCR correction
- PCR_correct_dropped_clonotypes: # of unique clonotypes dropped by PCR correction
- Fraction_Aligned_reads: fraction of total
- Fraction_Used_reads: fraction of total
- Fraction_PCR_correct_dropped_reads: fraction of total