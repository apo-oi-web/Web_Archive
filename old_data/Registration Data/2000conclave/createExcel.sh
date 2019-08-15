sed -e 's/^.*\ --\ /,/' current_reg.txt | perl csv.pl | sed -e 's/^,//'
