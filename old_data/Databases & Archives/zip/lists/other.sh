#!/bin/bash
rm -rf ~/public_html/lists/other/*

cat /shared/aliases/$1 >> ~/public_html/lists/other/data/$1
stat -c %U /shared/aliases/$1 >> ~/public_html/lists/other/owner/$1
date -r /shared/aliases/$1 >> ~/public_html/lists/other/time/$1

chmod +rx ~/public_html/lists/data/*
chmod +rx ~/public_html/lists/other/owner/*
chmod +rx ~/public_html/lists/other/time/*
