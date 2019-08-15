#!/bin/bash
rm -rf ~/public_html/publists/data/*
rm -rf ~/public_html/publists/owners/*
rm -rf ~/public_html/publists/times/*
rm -rf ~/public_html/publists/stat/*
rm -rf ~/public_html/publists/current.inc

for line in apo-alpha apo-bids apo-chairs apo-conclave apo-exec apo-fellowship apo-historian apo-membership apo-omegas apo-phi apo-pledgetrainer apo-pledges apo-pr apo-president apo-prospective apo-recruitment apo-secretary apo-sergeantatarms apo-service apo-slides apo-social apo-treasurer apo-underclassmen apoheadsofhouse execsnogeorge ift apo-oi-alumni freefood apo-brothers
do
	cat /shared/aliases/$line >> ~/public_html/publists/data/$line
	stat -c %U /shared/aliases/$line >> ~/public_html/publists/owners/$line
    	date -r /shared/aliases/$line >> ~/public_html/publists/times/$line
	stat /shared/aliases/$line >> ~/public_html/publists/stat/$line
done
echo "Data Last Updated: " >> ~/public_html/publists/current.inc
date > ~/public_html/publists/current.inc
chmod +rx ~/public_html/publists/data/*
chmod +rx ~/public_html/publists/owners/*
chmod +rx ~/public_html/publists/times/*
chmod +rx ~/public_html/publists/stat/*
chmod +rx ~/public_html/publists/current.inc
