import sys
import numpy as np

InfileName = sys.argv[1]
LengthsFileName = sys.argv[2]
outputfile = sys.argv[3]
logfile = "gLnotNormalized.log"

# open input file and create separate objects for the sample names and the abundance data (both starting from column 3). 
# ncols is used later to define the data range for creating a numpy array (see below)
with open (InfileName,'r') as f:
  samples = f.readline().split()[2:]
  ncols = len(f.readline().split('\t'))
  inputData = [l.strip('\n').split('\t') for l in f]
  f.close()

# create a dictionary from the ncbi genome lengths table (tab-delimited) with species name as key and a tuple (assembly-level,genome length) as value
with open (LengthsFileName,'r') as f:
  Genomelength = {key: value for (key, value) in [(l.strip('\n').split('\t')[0],(l.strip('\n').split('\t')[1],l.strip('\n').split('\t')[2])) for l in f]}
  f.close()

# create a dictionary from the previous one (Genomelength) reporting species names without further classifications (e.g. in strains), so take only genus and species from the keys of Genomelength. 
clean_species_names = {}
for eachElem in Genomelength.keys():
  clean_species_names[' '.join(eachElem.split()[0:2])]=eachElem

# GENUS MATCH REMOVED in v3
#clean_genus_names = {}
#for eachElem in Genomelength.keys():
  # no case-sensitive match of 'virus' and 'phage' to avoid assigning a virus to a bacterium genome size in the Genus search
#  if 'virus' not in eachElem.lower() and 'phage' not in eachElem.lower():
#    clean_genus_names[eachElem.split()[0]]=eachElem

# create an array with numpy including only the abundance data of the input file. 
# make the sum of species abundances for each samples (sum by column)
# make the sum of total species detected in the full dataset (used lated to get the % of not-normalized species)
data = np.loadtxt(InfileName, skiprows=1, delimiter='\t', usecols=range(2,ncols))
total_sample = data.sum(axis=0)
total_dataset = 0
for i in range(0, len(total_sample)):
  total_dataset = total_dataset + float(total_sample[i])

# Normalize with priority on Complete genomes (so as to normalize for the best assembly level available-following Kraken db of complege genomes and assemblies)
with open (outputfile,'w') as out, open (logfile,'w') as log:
  print ('\t'.join(['Species','ID','Assembly stage','Length (Mb)','Match']+samples),file=out)
#  print ('\t'.join(['Species','Total counts in full dataset','% abundance in full dataset'],file=log)
  for eachElem1 in inputData:
      if eachElem1[0] in Genomelength.keys() and Genomelength[eachElem1[0]][0]=='Complete':
          description = Genomelength[eachElem1[0]][0]
          length = Genomelength[eachElem1[0]][1]
          abund_orig = eachElem1[2:]
          abund_norm = [str(float(x)/float(length)) for x in abund_orig]
          print ('\t'.join([eachElem1[0],eachElem1[1],description,str(length),'exact']+abund_norm),file=out)

# Normalize with following best assembly priority: Chromosome 
      elif eachElem1[0] in Genomelength.keys() and Genomelength[eachElem1[0]][0]==' Chromosome':
          description = Genomelength[eachElem1[0]][0]
          length = Genomelength[eachElem1[0]][1]
          abund_orig = eachElem1[2:]
          abund_norm = [str(float(x)/float(length)) for x in abund_orig]
          print ('\t'.join([eachElem1[0],eachElem1[1],description,str(length),'exact']+abund_norm),file=out)

# Normalize with following best assembly priority: Scaffold 
      elif eachElem1[0] in Genomelength.keys() and Genomelength[eachElem1[0]][0]=='Scaffold':
          description = Genomelength[eachElem1[0]][0]
          length = Genomelength[eachElem1[0]][1]
          abund_orig = eachElem1[2:]
          abund_norm = [str(float(x)/float(length)) for x in abund_orig]
          print ('\t'.join([eachElem1[0],eachElem1[1],description,str(length),'exact']+abund_norm),file=out)

# Normalize with following best assembly priority: Contig 
      elif eachElem1[0] in Genomelength.keys() and Genomelength[eachElem1[0]][0]=='Contig':
          description = Genomelength[eachElem1[0]][0]
          length = Genomelength[eachElem1[0]][1]
          abund_orig = eachElem1[2:]
          abund_norm = [str(float(x)/float(length)) for x in abund_orig]
          print ('\t'.join([eachElem1[0],eachElem1[1],description,str(length),'exact']+abund_norm),file=out)

# If some strains or subspecies are not found in the gL list, mornalize them for the species (search in clean_species_names dictionary)
      elif ' '.join(eachElem1[0].split()[0:2]) in clean_species_names.keys():  
          description = Genomelength[clean_species_names[' '.join(eachElem1[0].split()[0:2])]][0]
          length = Genomelength[clean_species_names[' '.join(eachElem1[0].split()[0:2])]][1]
          abund_orig = eachElem1[2:]
          abund_norm = [str(float(x)/float(length)) for x in abund_orig]
          print ('\t'.join([eachElem1[0],eachElem1[1],description,str(length),'species']+abund_norm),file=out)

# GENUS MATCH REMOVED in v3    
#      elif eachElem1[0].split()[0] in clean_genus_names.keys():
#          description = Genomelength[clean_genus_names[eachElem1[0].split()[0]]][0]
#          length = Genomelength[clean_genus_names[eachElem1[0].split()[0]]][1]
#          abund_orig = eachElem1[2:]
#          abund_norm = [str(float(x)/float(length)) for x in abund_orig]
#          print ('\t'.join([eachElem1[0],eachElem1[1],description,str(length),'genus']+abund_norm),file=out)

# If a species is not found in the gL list (the two dictionaries created) print it with its % of representation in the overall abundance dataset.
      else:
          abund_orig = eachElem1[5:]
          sum = 0
          for i in range(0, len(abund_orig)):
            sum = sum + float(abund_orig[i])
          percent = (sum/total_dataset)*100
          print (eachElem1[0], sum, percent,file=log)
	
print ('Done!')