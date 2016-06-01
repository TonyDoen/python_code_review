 sed -i "s/,/;/g" `ls *.html`
 sed -i "s/style=\" height:25px; line-height:25px; padding:0 5px; text-align:left;\"//g" `ls *.html`
 sed -i "s/ //g" `ls *.html`
 sed -i ":label;N;s/\n//;b label" `ls *.html`
 #sed -i ":label;N;s/<\/tr>/\n/;b label" `ls *.html`
 sed -i "s/<td>//g" `ls *.html`
 sed -i "s/<\/td>/,/g" `ls *.html`
 sed -i "s/<\/tr>//g" `ls *.html`
 sed -i "s/<tr>/\n/g" `ls *.html`
 sed -ir '/^$/d' `ls *.html`
 sed -i '1d' `ls *.html`
