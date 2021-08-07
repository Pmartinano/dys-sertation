#!/bin/bash

INPUTDIR='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/DENOISED_HEAD_TORGO/MC01/Session3'
RESAMPLEDDIR='/mnt/c/Users/patri/OneDrive/Documentos/SLP/DISSERTATION/DENOISED_RESAMPLED_TORGO/MC01/Session3'

for i in ${INPUTDIR}/*.wav ; do
		BASE=`basename $i .wav` ;
			sox $i -r 22050 ${RESAMPLEDDIR}/${BASE}.wav ;	
			    done
			    


