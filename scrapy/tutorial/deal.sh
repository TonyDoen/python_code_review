#!/bin/bash

set -e

if [ -d "./html" ]; then
   rm -rf ./html
fi
mkdir ./html

mv ./*.html ./html
#if [ ! $? -eq 0 ]; then
#   exit 0
#fi

sed -i "s/,/;/g" `ls ./html/*.html`
sed -i "s/style=\" height:25px; line-height:25px; padding:0 5px; text-align:left;\"//g" `ls ./html/*.html`
sed -i "s/ //g" `ls ./html/*.html`
sed -i ":label;N;s/\n//;b label" `ls ./html/*.html`
#sed -i ":label;N;s/<\/tr>/\n/;b label" `ls ./html/*.html`
sed -i "s/<td>//g" `ls ./html/*.html`
sed -i "s/<\/td>/,/g" `ls ./html/*.html`
sed -i "s/<\/tr>//g" `ls ./html/*.html`
sed -i "s/<tr>/\n/g" `ls ./html/*.html`
sed -ir '/^$/d' `ls ./html/*.html`
sed -i '1d' `ls ./html/*.html`

cat `ls ./html/*.html` >> ./html/res.csv
sort ./html/res.csv | uniq > ./res.csv
