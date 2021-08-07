#!/bin/sh

INPUTDIR='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/2RNN/INPUT'
RESAMPLEDDIR='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/2RNN/RESAMPLEDIR'
OUTDIR='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/2RNN/OUTPUT'


for i in ${OUTDIR}/*.raw ; do
	    BASE=`basename $i .raw` ;
	        sox -v 3.33 -r 48000 -e signed-integer -b 16 -c 1 $i ${OUTDIR}/${BASE}.wav ;
	done

