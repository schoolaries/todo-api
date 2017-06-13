#!/bin/bash

choice=$1
argument1=$2
argument2=$3
argument3=$4
argument4=$5
if [ "$choice" == "print" ]
then
	python api5.py print > file.txt
elif [ "$choice" == "create" ]
then
	python api5.py create $argument1 $argument2 $argument3 > file.txt 
elif [ "$choice" == "update" ]
then
	python api5.py update $argument1 $argument2 $argument3 $argument4 > file.txt
elif [ "$choice" == "delete" ]
then
	python api5.py delete $argument1 > file.txt
fi
