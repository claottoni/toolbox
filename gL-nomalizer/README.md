# Genome length normalizer tool
Script to normalize a microbial species abundance table (generated from a full genomes database of taxonomic classifiers) for microbial genome lengths. 
Species names follows the NCBI taxonomy. 

The input is a tab-separated file with species names (following the NCBI taxonomy) in the first column, and the microbial abundances for each sample in the other columns. 

Use:
```
gL-normalizer-lite.py <input_table> prokaryotes_viruses_organelles.table <output_table>
```

The output is a tab-separated file reporting the Species-ID, the assembly stage of the genome in NCBI,  with the follo
```
ID	Assembly stage	Length (Mb)	Match	Sample_1	Sample_2	Sample_3
```
