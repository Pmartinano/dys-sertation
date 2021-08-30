#!/bin/bash
total=0
DIR=$1

for i in ${DIR}/*.wav; do
	RESULT=$(soxi -D "$i")
	total=$(echo "$total + $RESULT" | bc)
	echo $total
done
