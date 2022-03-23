#!/usr/bin/env Rscript

files = commandArgs(trailingOnly=TRUE)
tab1 = read.delim(files[1], header=T, fill=T, row.names=NULL, sep="\t")
names

# create vector of filenames (excluding the first already included as tab1.bracken) and loop through it
tabn = files[-1]
for (i in 1:length(tabn)){
  data = read.delim(tabn[i], header=T, fill=T, row.names=NULL, sep="\t")
  #data.bracken = data[,c(1,6)]
  #names(data) = c("taxon",basename(tabn[i]))
  # at first, merge the first two files, then merge all the rest
  if (!exists("tabfinal1")){
    tabfinal1 = merge(tab1, data, by=1, all=T)
    print(paste0("parsing ", files[c(1,2)]))
    } else {
  # merge all the others
  tabfinal1 = merge(tabfinal1, data, by=1, all=T)
  print(paste0("Merging ", tabn[i]))}
}
# remove NA
tabfinal1[is.na(tabfinal1)] <- 0
write.table(tabfinal1, file = 'abundance_table.merged', sep="\t", row.names=F, col.names=T, quote = FALSE)
