#!/usr/bin/env python

import sys

InfileName = sys.argv[1]
aroIndex = sys.argv[2]
#outputfile = sys.argv[3]

with open (InfileName,'r') as f:
  #samples = f.readline().split()[1:]
  inputData = [l.strip('\n').split('\t') for l in f]
  #print inputData
  #print accession
  f.close()

with open (aroIndex,'r') as f:
  aroFamily = {key: value for (key, value) in [(l.strip('\n').split('\t')[7],(l.strip('\n').split('\t')[8],l.strip('\n').split('\t')[9])) for l in f]}
  f.close()

for eachElem1 in inputData:
    readName = eachElem1[0]
    info = eachElem1[1]
    accession = info.split('|')[1]
    bitscore = eachElem1[11]
    if accession in aroFamily.keys():
    #if eachElem1[0] in aroFamily.keys():
        #AMRGeneFamily = aroFamily[eachElem1[0]][0]
        #ClassResistance = aroFamily[eachElem1[0]][1]
        AMRGeneFamily = aroFamily[accession][0]
        DrugClass = aroFamily[accession][1]
        #abund_norm = [str(float(x)/float(length)) for x in abund_orig]
        #print ('\t'.join([eachElem1[0],description,str(length),'exact']+abund_norm),file=out)
        print ("%s\t%s\t%s\t%s\t%s" % (readName,accession,bitscore,AMRGeneFamily,DrugClass))

