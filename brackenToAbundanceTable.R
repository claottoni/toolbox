#!/usr/bin/env Rscript

args = commandArgs(trailingOnly=TRUE)
dir = args[1]
files = list.files(path=dir, pattern="*.bracken$", full.names=T, recursive=F)
tab1 = read.delim(files[1], header=T, fill=T, row.names=NULL, sep="\t")

# create species names tables
# get columns 1 (species name) and 6 (bracken adjusted abundance)
tab1.bracken = tab1[,c(1,6)]
# assign column names from filenames
names(tab1.bracken) = c("taxon",basename(files[1]))
# create vector of filenames (excluding the first already included as tab1.bracken) and loop through it
tabn = files[-1]
for (i in 1:length(tabn)){
  data = read.delim(tabn[i], header=T, fill=T, row.names=NULL, sep="\t")
  data.bracken = data[,c(1,6)]
  names(data.bracken) = c("taxon",basename(tabn[i]))
  # at first, merge the first two files, then merge all the rest
  if (!exists("tabfinal1")){
    tabfinal1 = merge(tab1.bracken, data.bracken, by=1, all=T)
    print(paste0("parsing ", files[c(1,2)]))
    } else {
  # merge all the others
  tabfinal1 = merge(tabfinal1, data.bracken, by=1, all=T)
  print(paste0("parsing ", tabn[i]))}
}
# remove NA
tabfinal1[is.na(tabfinal1)] <- 0
write.table(tabfinal1, file = paste(dir,'taxa_abundance_bracken_names.txt',sep='/'),sep="\t",row.names=F, quote = FALSE)


files = list.files(path=dir, pattern="*.bracken$", full.names=T, recursive=F)
tab1 = read.delim(files[1], header=T, fill=T, row.names=NULL, sep="\t")
# create ncbi IDs table
tab2.bracken = tab1[,c(2,6)]
# assign column names from filenames
names(tab2.bracken) = c("ID",basename(files[1]))
for (i in 1:length(tabn)){
  data = read.delim(tabn[i], header=T, fill=T, row.names=NULL, sep="\t")
  data.bracken = data[,c(2,6)]
  names(data.bracken) = c("ID",basename(tabn[i]))
  # at first, merge the first two files, then merge all the rest
  if (!exists("tabfinal2")){
    tabfinal2 = merge(tab2.bracken, data.bracken, by=1, all=T)
    print(paste0("parsing ", files[c(1,2)]))
    } else {
  # merge all the others
  tabfinal2 = merge(tabfinal2, data.bracken, by=1, all=T)
  print(paste0("parsing ", tabn[i]))}
}
tabfinal2[is.na(tabfinal2)] <- 0
write.table(tabfinal2, file = paste(dir,'taxa_abundance_bracken_IDs.txt',sep='/'),sep="\t",row.names=F, quote = FALSE)
