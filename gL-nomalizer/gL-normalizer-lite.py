import sys

InfileName = sys.argv[1]
LengthsFileName = sys.argv[2]
outputfile = sys.argv[3]

with open (InfileName,'r') as f:
  samples = f.readline().split()[1:]
  inputData = [l.strip('\n').split('\t') for l in f]
  f.close()

with open (LengthsFileName,'r') as f:
  Genomelength = {key: value for (key, value) in [(l.strip('\n').split('\t')[0],(l.strip('\n').split('\t')[1],l.strip('\n').split('\t')[2])) for l in f]}
  f.close()

clean_species_names = {}
for eachElem in Genomelength.keys():
  clean_species_names[' '.join(eachElem.split()[0:2])]=eachElem

clean_genus_names = {}
for eachElem in Genomelength.keys():
  clean_genus_names[eachElem.split()[0]]=eachElem

with open (outputfile,'w') as out:
  print ('\t'.join(['ID','Assembly stage','Length (Mb)','Match']+samples),file=out)
  for eachElem1 in inputData:
      if eachElem1[0] in Genomelength.keys():
          description = Genomelength[eachElem1[0]][0]
          length = Genomelength[eachElem1[0]][1]
          abund_orig = eachElem1[1:]
          abund_norm = [str(float(x)/float(length)) for x in abund_orig]
          print ('\t'.join([eachElem1[0],description,str(length),'exact']+abund_norm),file=out)

      elif ' '.join(eachElem1[0].split()[0:2]) in clean_species_names.keys():  
          description = Genomelength[clean_species_names[' '.join(eachElem1[0].split()[0:2])]][0]
          length = Genomelength[clean_species_names[' '.join(eachElem1[0].split()[0:2])]][1]
          abund_orig = eachElem1[1:]
          abund_norm = [str(float(x)/float(length)) for x in abund_orig]

          print ('\t'.join([eachElem1[0],description,str(length),'species']+abund_norm),file=out)
      
      elif eachElem1[0].split()[0] in clean_genus_names.keys():
          description = Genomelength[clean_genus_names[eachElem1[0].split()[0]]][0]
          length = Genomelength[clean_genus_names[eachElem1[0].split()[0]]][1]
          abund_orig = eachElem1[1:]
          abund_norm = [str(float(x)/float(length)) for x in abund_orig]
          print ('\t'.join([eachElem1[0],description,str(length),'genus']+abund_norm),file=out)

print ('Done!')