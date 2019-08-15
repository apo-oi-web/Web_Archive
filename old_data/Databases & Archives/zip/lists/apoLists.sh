#!/bin/bash
rm -rf ~/public_html/lists/data/*
rm -rf ~/public_html/lists/owners/*
rm -rf ~/public_html/lists/times/*
rm -rf ~/public_html/lists/stat/*
rm -rf ~/public_html/lists/current.inc

for line in apo-alpha apo-bids apo-chairs apo-conclave apo-exec apo-fellowship apo-historian apo-membership apo-omegas apo-phi apo-pledgetrainer apo-pledges apo-pr apo-president apo-prospective apo-recruitment apo-secretary apo-sergeantatarms apo-service apo-slides apo-social apo-treasurer apo-underclassmen apoheadsofhouse execsnogeorge ift apo-oi-alumni freefood apo-brothers
do
	cat /shared/aliases/$line >> ~/public_html/lists/data/$line
	stat -c %U /shared/aliases/$line >> ~/public_html/lists/owners/$line
    	date -r /shared/aliases/$line >> ~/public_html/lists/times/$line
	stat /shared/aliases/$line >> ~/public_html/lists/stat/$line
done
echo "Data Last Updated: " >> ~/public_html/lists/current.inc
date > ~/public_html/lists/current.inc
chmod +rx ~/public_html/lists/data/*
chmod +rx ~/public_html/lists/owners/*
chmod +rx ~/public_html/lists/times/*
chmod +rx ~/public_html/lists/stat/*
chmod +rx ~/public_html/lists/current.inc
