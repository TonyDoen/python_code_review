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
sed -i "s//|/g" `ls ./html/*.html`

cat `ls ./html/*.html` >> ./html/res.csv
echo " 姓名,报考学校,报考专业,专业门类,总分,政治,外语,专一,专二,电话,邮箱,调剂意向,发布时间, " > ./html/tmp.csv
sort ./html/res.csv | uniq >> ./html/tmp.csv
#iconv -f UTF-8 -t GBK ./html/tmp.csv > ./res.csv
