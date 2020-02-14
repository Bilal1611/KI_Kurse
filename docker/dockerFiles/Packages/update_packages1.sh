#!/bin/bash
for i in $(cat $1); do
	if [[ "$i" == *"anaconda"* ]]; then
		echo "#RUN pip install $i"   
	else	
		echo "RUN pip install $i"
	fi
done
