#!/bin/bash

echo "Are you sure to clean up all files in recycle bin (y/n)?"
read a

if [[ "$a" == 'y' ]] || [[ "$a" == 'yes' ]] || [[ "$a" == 'Y' ]] || [[ "$a" == 'Yes' ]] || [[ "$a" == 'YES' ]];
then
    rm -rf ~/recyclebin/*
    echo "Recyclebin is cleaned up."

fi
exit 0
