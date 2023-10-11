# Genome length normalizer tool
Script used to normalize a microbial species abundance table (generated from a full genomes database of taxonomic classifiers) for microbial genome lengths. 
Species names follows the NCBI taxonomy. 

The input is a tab-separated file with species names (following the NCBI taxonomy) in the first column, and the microbial abundances for each sample in the other columns. 

Use:
```
gL-normalizer-lite.py <input_table> prokaryotes_viruses_organelles.table <output_table>
```

The output is a tab-separated file reporting from the first coulumn the Species-ID, the assembly stage of the genome in NCBI, the match level ('exact' when it's at the species level, otherwise 'genus' when a species is missing and a random species with a complete genome of the same genus is used), and the normalized abundaces for each sample.
```
ID	Assembly stage	Length (Mb)	Match	Sample_1	Sample_2	Sample_3
```
