#!/bin/bash

INPUTDIR='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/2RNN/INPUT'
RESAMPLEDDIR='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/2RNN/RESAMPLEDIR'
OUTDIR='/mnt/c/Users/patri/OneDrive/Documents/SLP/DISSERTTION/2RNN/OUTPUT'

for i in ${INPUTDIR}/*.wav ; do
	BASE=`basename $i .wav` ;
	sox -v 0.3 $i -t sw -r 48000 -c 1 ${RESAMPLEDDIR}/${BASE}.raw ;	
    done

