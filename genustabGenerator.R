args = commandArgs(trailingOnly=TRUE)
file = args[1]


#import table
tab = read.delim("abundance_table.merged.taxonomy.final.noVirus", header=T, fill=T, row.names=NULL, sep="\t")
#select genus column and abundance data columns
tab.genus = tab[,c(17,20:ncol(tab))]
#aggregate table
tab.agg = aggregate(.~genus, tab.genus, sum)
#save file
write.table(tab.agg,"abundance_table.merged.final",sep="\t",row.names=F,col.names=TRUE,quote=FALSE)



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
