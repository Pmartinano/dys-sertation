#!/bin/bash

INPUTDIR='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/2RNN/INPUT'
RESAMPLEDDIR='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/2RNN/RESAMPLEDIR'
OUTPUT='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/2RNN/OUTPUT'

for i in ${RESAMPLEDDIR}/*.raw ; do
	    BASE=`basename $i .raw` ;
	        ./examples/rnnoise_demo $i ${OUTPUT}/${BASE}.raw ;
	done
