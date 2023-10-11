#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)
dir = args[1]
files <- list.files(path=dir, pattern="*.bed$", full.names=T,recursive=FALSE)

outfile = c()
for (i in files) {
tab=read.table(i)
table(tab$V2)
t=diff(table(tab$V2))
delta=sum(t[which(t<0)])/sum(abs(t))
print (paste (i, delta))
outfile = rbind(outfile, c(i, delta))
}
write.table(outfile, file = paste(dir,'delta_table.txt',sep = '/'), sep=";", row.names=FALSE)
