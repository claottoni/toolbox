#!/bin/bash

usage="$(basename "$0") [-h] [-i <string>]
    -h  show this help text
    -i  <string> path to file abundance table"


while getopts ":hi::" option
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
awk -F'\t' '{print $2}' $INFILE | tail -n +2 > ${INFILE}.idncbi
echo "Running taxaranks"
taxaranks -i ${INFILE}.idncbi -o ${INFILE}.taxonomy
echo "Parsing final table"
paste ${INFILE}.taxonomy ${INFILE} > ${INFILE}.taxonomy.final
