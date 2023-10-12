#!/usr/bin/env python

import re
import sys
import os

FileList = sys.argv[1:]
Header = 0
for InfileName in FileList:
  if Header == 0:
    Header = "Sample\tHits\tTotalReads\tcpmNormalizedReads" 
    print (Header)
    Infile = open(InfileName, 'r')
    ReadsName = []
    for line in Infile:
      line = line.strip('\n')
      element = line.split('\t')
      ReadsName.append(element[0])
    Hits = len(sorted(set(ReadsName)))
    FastaName = InfileName.replace("aro.blastn.out", "fasta")
    FastaFile = open(FastaName, 'r')
    TotalReads = len([1 for line in open(FastaName) if line.startswith(">")])
    NormalizedReads = Hits / TotalReads * 1000000
    print ("%s\t%s\t%s\t%f" % (os.path.basename(InfileName), Hits, TotalReads, NormalizedReads))
  else:
    Infile=open(InfileName, 'r')
    ReadsName = []
    for line in Infile:
      line = line.strip('\n')
      element = line.split('\t')
      ReadsName.append(element[0])
    Hits = len(sorted(set(ReadsName)))
    FastaName = InfileName.replace("aro.blastn.out", "fasta")
    FastaFile = open(FastaName, 'r')
    TotalReads = len([1 for line in open(FastaName) if line.startswith(">")])	
    NormalizedReads = Hits / TotalReads * 1000000
    print ("%s\t%s\t%s\t%f" % (os.path.basename(InfileName), Hits, TotalReads, NormalizedReads))
