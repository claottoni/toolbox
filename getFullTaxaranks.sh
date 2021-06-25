#!/bin/bash

usage="$(basename "$0") [-h] [-i <string>]
    -h  show this help text
    -t  <string> path to file accessionTaxa.sql"


while getopts ":hi:t::" option
do
  case $option in
    i) INFILE=${OPTARG};;
    h) echo "$usage"
       exit;;
    *) echo "$usage"
       exit 1;;
  esac
done


# AUTOMATE SCRIPT

OUTDIR=$(dirname $INFILE)
filename=$(basename $INFILE)
#fname="${filename%.txt}"


echo "Getting species list"
awk -F'\t' '{print $1}' $INFILE | tail -n +2 > ${INFILE}.species
echo "Running taxaranks"
taxaranks -i ${INFILE}.species -o ${INFILE}.taxonomy
echo "Parsing final table"
paste ${INFILE}.taxonomy ${INFILE} > ${INFILE}.taxonomy.final
